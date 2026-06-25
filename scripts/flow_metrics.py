#!/usr/bin/env python3
"""Flow-metrics analyzer — SP-free delivery footprint (플로우 지표 분석기 — SP 없이도).

Part of the "aligned-delivery" skill. The other scripts lean on **story points**
(predictability, fragmentation = tickets/SP, per-capita SP). But SP — and due
dates — are not universal: many teams run an issue tracker with no estimation at
all. This script reads the **universal footprint (도)** instead — the data every
issue tracker already emits: timestamps and counts. No SP, no due dates required.

It surfaces the flow + stability signals distilled from general flow/DORA practice.
These map onto **DORA's four keys**: the first block is the SPEED half (throughput /
lead / cycle / flow efficiency); the second block is the STABILITY half (deployment
frequency, change failure rate, MTTR). (DORA 4대 지표 — 속도 절반 + 안정성 절반.)

SPEED (속도):
    • throughput      — completed tickets per period (the SP-free volume measure)
    • lead time       — created → resolved (the customer-facing wait, queue + work)
    • cycle time      — work-started → resolved (active work time only)
    • flow efficiency — cycle / lead (how much of the wait was actual work vs queue)

STABILITY (안정성) — DORA's other two keys, plus deployment frequency:
    • deployment frequency — deploys to production per period (배포 빈도)
    • change failure rate  — failures / deploys (변경 실패율)
    • MTTR                 — mean time to restore service, from restore_hours (복구 시간)

Read these as 도 (footprint/trajectory). Low flow efficiency = the system spends
its time *waiting in queues*, a structural (리) / cooperation-layer (공조) signal,
not a "work faster" problem. Rising lead time and volatile throughput echo the
volatility-as-debt rule. And on the speed↔stability tie: a rising deployment
frequency *with* a rising change-failure-rate is NOT a win — it is shipping
instability faster (속도와 안정성의 결합: 배포 빈도↑ + 변경 실패율↑ 는 성과가 아님).
(지표는 도(흔적). 낮은 플로우 효율 = 큐 대기 = 리/공조층 신호.)

------------------------------------------------------------------------------
INPUT CSV COLUMNS (열 이름) — one row per COMPLETED ticket:
    period   : the time bucket (e.g. 2026-01 or a sprint id). REQUIRED — used to
               align the throughput / lead-time series.
    role     : role or person (frontend, backend, design, a name). OPTIONAL — adds
               a per-role breakdown; absent → whole-team only.
    created  : when the ticket was created/requested (ISO date). OPTIONAL — with
               'resolved' gives LEAD time; absent → lead-time analysis skipped.
    started  : when active work began (ISO date). OPTIONAL — with 'resolved' gives
               CYCLE time; absent → cycle-time analysis skipped.
    resolved : when the ticket was completed (ISO date). OPTIONAL — needed for lead
               and cycle time; absent → only throughput (row counts) is computed.
    deploys       : number of production deployments in the period (count). OPTIONAL —
               drives deployment frequency; absent → DORA stability skipped.
    failures      : number of deployments/changes that caused a failure or incident in
               the period (count). OPTIONAL — with 'deploys' gives change failure rate.
    restore_hours : hours to restore service for incidents in the period. OPTIONAL —
               drives MTTR. CHOICE: the row value is read as the period's MEAN restore
               time (per incident); MTTR is then the mean across periods. If your data
               is a per-period total instead, divide by incident count before loading.

Dates accept YYYY-MM-DD or YYYY-MM-DD HH:MM[:SS]. Throughput needs only
period (+ optional role); everything time-based degrades gracefully (skips with a
warning) when its columns are absent — so a bare period,role CSV still works.

The stability columns (deploys, failures, restore_hours) are PERIOD-LEVEL, not
per-ticket: they repeat the same value on every row of a period, so the script
reads the first non-blank value seen per period. A CSV with no deploy column just
skips the DORA stability section (warn, don't crash).

This consumes an ALREADY-NORMALIZED CSV. Mapping an arbitrary Jira export onto
these columns (header names vary per org) is the caller's job — see the "Jira
ingestion" protocol in SKILL.md. Source/Jira data is confidential: keep it in a
gitignored workspace and strip org/person identifiers.

SAMPLE CSV (샘플):
    period,role,created,started,resolved,deploys,failures,restore_hours
    2026-01,backend,2026-01-02,2026-01-08,2026-01-12,8,1,3.5
    2026-01,frontend,2025-12-20,2026-01-10,2026-01-14,8,1,3.5
    2026-02,backend,2026-01-28,2026-02-03,2026-02-06,12,2,4.0
    2026-02,frontend,2026-01-15,2026-02-01,2026-02-11,12,2,4.0

USAGE (사용법):
    python3 flow_metrics.py sample_flow.csv
    python3 flow_metrics.py --help

THRESHOLDS (임계값) — general flow/DORA priors, NOT the 26-month dataset; treat as
direction, re-verify on your data (일반 flow/DORA prior — 방향으로, 본인 데이터로 재검증):
    Flow efficiency = cycle / lead.  < ~40% => most time is queue/wait, not work —
        a structural/cooperation signal, not a "work harder" one.
    Throughput volatility = CV across periods.  > ~0.5 => unstable flow (ties to the
        volatility-as-debt rule; stability > heroics).
    Lead-time trend: latest-period median > ~1.5× earliest => a growing queue (도);
        directional, read alongside throughput.
    Change failure rate > ~15% => DORA's "medium/low" band. This 15% is an INDUSTRY
        PRIOR (from DORA reports), NOT this skill's dataset — read as direction only.

EXIT CODES:
    0 success ; 1 missing/unreadable file or no usable rows.
"""

import argparse
import csv
import datetime
import statistics
import sys

# ---- Thresholds (priors — see docstring) -----------------------------------
FLOW_EFF_LOW = 0.40        # cycle/lead below this => queue-dominated
THROUGHPUT_CV_HI = 0.50    # CV of throughput across periods => unstable flow
LEAD_TREND_RATIO = 1.50    # latest median / earliest median above this => rising
CHANGE_FAIL_HI = 0.15      # change failure rate above this => DORA medium/low band
                           # (INDUSTRY PRIOR from DORA reports, NOT this skill's data)

_DATE_FORMATS = ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d")


def parse_num(s):
    """Parse a non-negative number; return float or None (robust to blanks/junk)."""
    s = (s or "").strip()
    if not s:
        return None
    try:
        v = float(s)
    except ValueError:
        return None
    return v if v >= 0 else None


def parse_date(s):
    """Parse an ISO-ish date; return a datetime or None (robust to blanks/junk)."""
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.datetime.fromisoformat(s)
    except ValueError:
        pass
    for fmt in _DATE_FORMATS:
        try:
            return datetime.datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def load_rows(path):
    """Read the CSV → (rows, flags dict). Warns + skips bad rows, never crashes."""
    try:
        f = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        sys.stderr.write("ERROR: file not found (파일 없음): %s\n" % path)
        sys.exit(1)
    except OSError as exc:
        sys.stderr.write("ERROR: cannot read file (읽기 실패): %s (%s)\n" % (path, exc))
        sys.exit(1)

    rows = []
    with f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            sys.stderr.write("ERROR: empty CSV (빈 파일): %s\n" % path)
            sys.exit(1)
        cols = {c.strip().lower() for c in reader.fieldnames if c}
        if "period" not in cols:
            sys.stderr.write("ERROR: missing required column 'period' (필수 열 누락: period).\n")
            sys.exit(1)
        has_role = "role" in cols
        has_created = "created" in cols
        has_started = "started" in cols
        has_resolved = "resolved" in cols
        has_deploys = "deploys" in cols
        has_failures = "failures" in cols
        has_restore = "restore_hours" in cols
        if not has_deploys:
            sys.stderr.write(
                "WARNING: no 'deploys' column — DORA stability section "
                "(deploy frequency / change failure rate) skipped "
                "(deploys 열 없음 — DORA 안정성 생략).\n")
        if not has_restore:
            sys.stderr.write(
                "WARNING: no 'restore_hours' column — MTTR skipped "
                "(restore_hours 열 없음 — MTTR 생략).\n")
        if not has_resolved:
            sys.stderr.write(
                "WARNING: no 'resolved' column — only throughput (counts) computed; "
                "lead/cycle time skipped (resolved 열 없음 — 처리량만 계산).\n")
        else:
            if not has_created:
                sys.stderr.write(
                    "WARNING: no 'created' column — lead-time analysis skipped "
                    "(created 열 없음 — 리드타임 생략).\n")
            if not has_started:
                sys.stderr.write(
                    "WARNING: no 'started' column — cycle-time analysis skipped "
                    "(started 열 없음 — 사이클타임 생략).\n")

        for lineno, raw in enumerate(reader, start=2):
            r = {(k.strip().lower() if k else k): v for k, v in raw.items()}
            period = (r.get("period") or "").strip()
            if not period:
                sys.stderr.write("WARNING: line %d skipped — blank period.\n" % lineno)
                continue
            row = {
                "period": period,
                "role": (r.get("role") or "").strip() if has_role else "",
                "created": parse_date(r.get("created")) if has_created else None,
                "started": parse_date(r.get("started")) if has_started else None,
                "resolved": parse_date(r.get("resolved")) if has_resolved else None,
                "deploys": parse_num(r.get("deploys")) if has_deploys else None,
                "failures": parse_num(r.get("failures")) if has_failures else None,
                "restore_hours": parse_num(r.get("restore_hours")) if has_restore else None,
            }
            rows.append(row)

    if not rows:
        sys.stderr.write("ERROR: no valid data rows (유효 데이터 없음).\n")
        sys.exit(1)
    flags = {
        "has_role": has_role, "has_created": has_created,
        "has_started": has_started, "has_resolved": has_resolved,
        "has_deploys": has_deploys, "has_failures": has_failures,
        "has_restore": has_restore,
    }
    return rows, flags


def _days(a, b):
    """Whole-day difference b - a, or None if either is missing or b < a."""
    if a is None or b is None:
        return None
    d = (b - a).total_seconds() / 86400.0
    return d if d >= 0 else None


def fmt(x, nd=2):
    if x is None:
        return "n/a"
    return ("%." + str(nd) + "f") % x


def analyze(rows, flags):
    periods = sorted({r["period"] for r in rows})
    roles = sorted({r["role"] for r in rows if r["role"]}) if flags["has_role"] else []

    # Throughput: completed-ticket count per period (and per role).
    throughput = {p: sum(1 for r in rows if r["period"] == p) for p in periods}
    throughput_by_role = {}
    if roles:
        for role in roles:
            throughput_by_role[role] = {
                p: sum(1 for r in rows if r["period"] == p and r["role"] == role)
                for p in periods
            }

    tput_vals = [throughput[p] for p in periods]
    tput_mean = statistics.fmean(tput_vals) if tput_vals else 0.0
    tput_stdev = statistics.stdev(tput_vals) if len(tput_vals) > 1 else 0.0
    tput_cv = (tput_stdev / tput_mean) if tput_mean > 0 else None

    # Lead / cycle time per period (median is robust to outliers).
    lead_by_period = {}
    cycle_by_period = {}
    for p in periods:
        rr = [r for r in rows if r["period"] == p]
        leads = [d for d in (_days(r["created"], r["resolved"]) for r in rr) if d is not None]
        cycles = [d for d in (_days(r["started"], r["resolved"]) for r in rr) if d is not None]
        lead_by_period[p] = statistics.median(leads) if leads else None
        cycle_by_period[p] = statistics.median(cycles) if cycles else None

    all_leads = [d for d in (_days(r["created"], r["resolved"]) for r in rows) if d is not None]
    all_cycles = [d for d in (_days(r["started"], r["resolved"]) for r in rows) if d is not None]
    lead_med = statistics.median(all_leads) if all_leads else None
    cycle_med = statistics.median(all_cycles) if all_cycles else None
    flow_eff = (cycle_med / lead_med) if (lead_med and cycle_med is not None and lead_med > 0) else None

    # Lead-time trend: earliest vs latest period with a lead-time value.
    lead_series = [(p, lead_by_period[p]) for p in periods if lead_by_period[p] is not None]
    lead_trend = None
    if len(lead_series) >= 2:
        first_v = lead_series[0][1]
        last_v = lead_series[-1][1]
        if first_v and first_v > 0:
            lead_trend = last_v / first_v

    # --- DORA STABILITY (period-level: first non-blank value seen per period) ---
    def _first(p, key):
        for r in rows:
            if r["period"] == p and r.get(key) is not None:
                return r[key]
        return None

    deploys_by_period = {p: _first(p, "deploys") for p in periods} if flags["has_deploys"] else {}
    failures_by_period = {p: _first(p, "failures") for p in periods} if flags["has_failures"] else {}
    restore_by_period = {p: _first(p, "restore_hours") for p in periods} if flags["has_restore"] else {}

    # Change failure rate per period = failures / deploys (only where both present & deploys>0).
    cfr_by_period = {}
    for p in periods:
        d = deploys_by_period.get(p)
        fcount = failures_by_period.get(p)
        if d is not None and d > 0 and fcount is not None:
            cfr_by_period[p] = fcount / d

    deploy_vals = [v for v in deploys_by_period.values() if v is not None]
    deploy_mean = statistics.fmean(deploy_vals) if deploy_vals else None
    deploy_total = sum(deploy_vals) if deploy_vals else None

    total_deploys = sum(v for v in deploys_by_period.values() if v is not None)
    total_failures = sum(v for v in failures_by_period.values() if v is not None)
    cfr_overall = (total_failures / total_deploys) if total_deploys > 0 else None

    restore_vals = [v for v in restore_by_period.values() if v is not None]
    mttr = statistics.fmean(restore_vals) if restore_vals else None

    return {
        "periods": periods, "roles": roles,
        "throughput": throughput, "throughput_by_role": throughput_by_role,
        "tput_mean": tput_mean, "tput_stdev": tput_stdev, "tput_cv": tput_cv,
        "lead_by_period": lead_by_period, "cycle_by_period": cycle_by_period,
        "lead_med": lead_med, "cycle_med": cycle_med, "flow_eff": flow_eff,
        "lead_trend": lead_trend,
        "deploys_by_period": deploys_by_period, "deploy_mean": deploy_mean,
        "deploy_total": deploy_total, "cfr_by_period": cfr_by_period,
        "cfr_overall": cfr_overall, "mttr": mttr,
        "restore_by_period": restore_by_period,
    }


def report(a, flags):
    out = []
    w = out.append
    flags_msgs = []

    w("=" * 70)
    w("FLOW METRICS REPORT (플로우 지표 리포트) — DORA 4 keys, SP-free footprint (도)")
    w("=" * 70)
    w("Periods (기간): %d   |   Roles (역할): %d   |   completed tickets: %d"
      % (len(a["periods"]), len(a["roles"]), sum(a["throughput"].values())))
    w("")

    # --- Throughput ---
    w("-" * 70)
    w("1. THROUGHPUT = completed tickets / period (처리량 — SP 불요)")
    w("-" * 70)
    for p in a["periods"]:
        w("  %-12s tickets (티켓): %d" % (p, a["throughput"][p]))
    if a["roles"]:
        w("  by role (직군별):")
        for role in a["roles"]:
            series = ", ".join("%s=%d" % (p, a["throughput_by_role"][role][p])
                               for p in a["periods"])
            w("    %-12s %s" % (role, series))
    w("  mean (평균): %s   STDEV (표준편차): %s" % (fmt(a["tput_mean"]), fmt(a["tput_stdev"])))
    cv = a["tput_cv"]
    if cv is None:
        w("  volatility CV (변동계수): n/a")
    else:
        tag = "[unstable / 불안정]" if cv > THROUGHPUT_CV_HI else "[stable / 안정]"
        w("  volatility CV (변동계수): %s %s" % (fmt(cv), tag))
        if cv > THROUGHPUT_CV_HI:
            flags_msgs.append("THROUGHPUT VOLATILITY (처리량 변동성): CV %s > %s — "
                              "volatility is debt; stability > heroics (변동성=부채, 안정>영웅)."
                              % (fmt(cv), fmt(THROUGHPUT_CV_HI, 1)))
    w("")

    # --- Lead time ---
    w("-" * 70)
    w("2. LEAD TIME = created → resolved, days (리드타임 — 요청부터 완료까지, 일)")
    w("-" * 70)
    if not flags["has_resolved"] or not flags["has_created"] or a["lead_med"] is None:
        w("  (skipped — needs 'created' + 'resolved' / created·resolved 필요로 생략)")
    else:
        for p in a["periods"]:
            w("  %-12s median lead (중앙값): %s d" % (p, fmt(a["lead_by_period"][p])))
        w("  OVERALL median lead (전체 중앙값): %s d" % fmt(a["lead_med"]))
        lt = a["lead_trend"]
        if lt is not None:
            tag = "[rising queue / 큐 증가]" if lt > LEAD_TREND_RATIO else "[steady / 안정]"
            w("  trend latest/earliest (추세 최근/최초): %sx %s" % (fmt(lt), tag))
            if lt > LEAD_TREND_RATIO:
                flags_msgs.append("RISING LEAD TIME (리드타임 상승): %sx earliest — "
                                  "queue growing; work waits longer before done "
                                  "(큐 증가, 완료 전 대기↑)." % fmt(lt))
    w("")

    # --- Cycle time ---
    w("-" * 70)
    w("3. CYCLE TIME = started → resolved, days (사이클타임 — 착수부터 완료까지, 일)")
    w("-" * 70)
    if not flags["has_resolved"] or not flags["has_started"] or a["cycle_med"] is None:
        w("  (skipped — needs 'started' + 'resolved' / started·resolved 필요로 생략)")
    else:
        for p in a["periods"]:
            w("  %-12s median cycle (중앙값): %s d" % (p, fmt(a["cycle_by_period"][p])))
        w("  OVERALL median cycle (전체 중앙값): %s d" % fmt(a["cycle_med"]))
    w("")

    # --- Flow efficiency ---
    w("-" * 70)
    w("4. FLOW EFFICIENCY = cycle / lead (플로우 효율 — 실작업/총대기)")
    w("-" * 70)
    fe = a["flow_eff"]
    if fe is None:
        w("  (skipped — needs both lead & cycle / 리드·사이클 둘 다 필요)")
    else:
        tag = "[queue-dominated / 큐 지배]" if fe < FLOW_EFF_LOW else "[ok]"
        w("  flow efficiency (플로우 효율): %s%% %s" % (fmt(fe * 100, 0), tag))
        w("  (the rest is queue/wait, not active work / 나머지는 큐·대기)")
        if fe < FLOW_EFF_LOW:
            flags_msgs.append("LOW FLOW EFFICIENCY (낮은 플로우 효율): %s%% < %s%% — most "
                              "time is queue, not work: a structure/cooperation signal, "
                              "not 'work faster' (대부분 큐 대기 — 구조·공조 신호, 속도 문제 아님)."
                              % (fmt(fe * 100, 0), fmt(FLOW_EFF_LOW * 100, 0)))
    w("")

    # --- DORA stability (deployment frequency / change failure rate / MTTR) ---
    w("-" * 70)
    w("5. DORA STABILITY = deploy freq · change failure rate · MTTR (안정성)")
    w("-" * 70)
    if not flags["has_deploys"] and not flags["has_restore"]:
        w("  (skipped — needs 'deploys' and/or 'restore_hours' / "
          "deploys·restore_hours 필요로 생략)")
    else:
        # Deployment frequency
        if flags["has_deploys"] and a["deploy_mean"] is not None:
            w("  5a. Deployment frequency = deploys / period (배포 빈도):")
            for p in a["periods"]:
                dv = a["deploys_by_period"].get(p)
                w("      %-12s deploys (배포): %s" % (p, fmt(dv, 0) if dv is not None else "n/a"))
            w("      mean per period (기간 평균): %s   total (총): %s"
              % (fmt(a["deploy_mean"], 1), fmt(a["deploy_total"], 0)))
        else:
            w("  5a. Deployment frequency (배포 빈도): (skipped — no 'deploys' / deploys 없음)")
        # Change failure rate
        cfr = a["cfr_overall"]
        if flags["has_deploys"] and flags["has_failures"] and cfr is not None:
            w("  5b. Change failure rate = failures / deploys (변경 실패율):")
            for p in a["periods"]:
                pv = a["cfr_by_period"].get(p)
                w("      %-12s rate (실패율): %s"
                  % (p, (fmt(pv * 100, 0) + "%") if pv is not None else "n/a"))
            tag = "[high — DORA medium/low band / 높음]" if cfr > CHANGE_FAIL_HI else "[ok]"
            w("      OVERALL (전체): %s%% %s" % (fmt(cfr * 100, 0), tag))
            if cfr > CHANGE_FAIL_HI:
                flags_msgs.append("HIGH CHANGE FAILURE RATE (높은 변경 실패율): %s%% > %s%% "
                                  "(industry prior, not this skill's data) — shipping faster "
                                  "is no win if more ships break (업계 prior, 본 스킬 데이터 아님 — "
                                  "빨리 배포해도 깨지면 성과 아님)."
                                  % (fmt(cfr * 100, 0), fmt(CHANGE_FAIL_HI * 100, 0)))
        else:
            w("  5b. Change failure rate (변경 실패율): (skipped — needs 'deploys'+'failures' / "
              "deploys·failures 필요)")
        # MTTR
        if flags["has_restore"] and a["mttr"] is not None:
            w("  5c. MTTR = mean time to restore, hours (평균 복구 시간, 시간):")
            for p in a["periods"]:
                rv = a["restore_by_period"].get(p)
                w("      %-12s restore (복구): %s"
                  % (p, (fmt(rv, 1) + " h") if rv is not None else "n/a"))
            w("      MTTR mean across periods (기간 평균): %s h" % fmt(a["mttr"], 1))
            w("      (row value read as period MEAN restore time per incident / "
              "행 값 = 인시던트당 기간 평균 복구 시간)")
        else:
            w("  5c. MTTR (복구 시간): (skipped — no 'restore_hours' / restore_hours 없음)")
        # The speed<->stability tie.
        w("")
        w("  READ (해석): speed + stability are ONE story — a rising deployment frequency")
        w("  WITH a rising change-failure-rate is not a win, it ships instability faster.")
        w("  (속도와 안정성은 한 몸 — 배포 빈도↑ 인데 변경 실패율↑ 면 성과가 아니라")
        w("  불안정을 더 빨리 내보내는 것.)")
    w("")

    # --- Flags ---
    w("=" * 70)
    w("FLAGS (위험 신호 요약)")
    w("=" * 70)
    if not flags_msgs:
        w("  None — flow is steady (모두 양호: 흐름 안정).")
    else:
        for fl in flags_msgs:
            w("  [!] " + fl)
    w("  (thresholds are general flow/DORA priors — read as direction, re-verify on "
      "your data / 임계값은 일반 prior — 방향으로 읽고 본인 데이터로 재검증.)")
    w("=" * 70)
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Flow-metrics analyzer (플로우 지표 분석기) — SP-free footprint + "
                    "DORA's four keys: SPEED (throughput, lead time, cycle time, flow "
                    "efficiency) and STABILITY (deployment frequency, change failure "
                    "rate, MTTR) from timestamps + counts. No story points / due dates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="CSV columns (열): period(required); role/created/started/resolved "
               "(optional, dates); deploys/failures/restore_hours (optional, counts).\n"
               "Thresholds: flow-eff<40%=queue-dominated; throughput CV>0.5=unstable; "
               "lead trend>1.5x=rising queue; change-failure-rate>15%=DORA medium/low "
               "band (industry prior, not this skill's data).",
    )
    parser.add_argument("csv_path", help="path to the flow CSV (플로우 CSV 경로)")
    args = parser.parse_args(argv)

    rows, flags = load_rows(args.csv_path)
    a = analyze(rows, flags)
    print(report(a, flags))
    return 0


if __name__ == "__main__":
    sys.exit(main())
