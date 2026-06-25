#!/usr/bin/env python3
"""Workload distribution & fragmentation analyzer (워크로드 분포·파편화 분석기).

Part of the "aligned-delivery" skill. Grounded in N2C / Dynamic Resonance
Ontology — specifically the cooperation layer (공조층): roles should cooperate,
not silo. This script reads completed-work data per role (or per person) over
time and surfaces three operating risks distilled from 26 months of product-team
data: over-fragmentation, role silos, and workload imbalance.

------------------------------------------------------------------------------
INPUT CSV COLUMNS (열 이름):
    role     : the role or person (e.g. frontend, backend, design, or a name)
    period   : the time bucket (e.g. sprint or month) — used to align series
    sp       : total completed story points that period
    tickets  : completed ticket count that period
    ops_sp   : story points spent on operations/maintenance (a SUBSET of sp).
               OPTIONAL — if the column is absent, the ops-ratio analysis is
               skipped with a warning instead of crashing.
    headcount: number of people in this role for this period. OPTIONAL — when
               present, workload imbalance is measured PER-CAPITA (team-size
               adjusted); when absent it falls back to raw total SP (which a
               larger role inflates) with a warning.

This script consumes an ALREADY-NORMALIZED CSV. Mapping an arbitrary Jira
export onto these columns (header names vary per org; ops classification by
epic / type / label / title keyword / reverse-inference from child tickets) is
the caller's job — see the "Jira ingestion" protocol in SKILL.md. Source/Jira
data is confidential: keep it in a gitignored workspace, strip org identifiers.

SAMPLE CSV (샘플):
    role,period,sp,tickets,ops_sp
    frontend,2026-01,20,10,4
    frontend,2026-02,18,9,5
    backend,2026-01,22,11,18
    backend,2026-02,21,30,19
    design,2026-01,12,8,2
    design,2026-02,14,7,3

USAGE (사용법):
    python3 workload_fragmentation.py sample_workload.csv
    python3 workload_fragmentation.py --help

THRESHOLDS (임계값):
    Fragmentation index = tickets / SP.  > 2.0  => over-fragmentation (과파편).
        (Ideal work item ~0.5 SP; context-switching cuts effective output by
         roughly 1/6 when over-fragmented.)
    Operations ratio    = ops_sp / sp.   > 50% => silo risk (사일로 위험).
        Healthy band ~25-35% (건강 구간).
    Cross-role correlation (avg pairwise Pearson on per-period SP):
        < 0.1 => silo risk (사일로 위험) — roles moving independently.
    Workload imbalance: coefficient of variation across roles of per-capita SP
        (or raw total SP if no headcount column).
        CV > 0.5 => high imbalance (불균형) flagged as delivery debt.
        NOTE: raw-total CV is confounded by team size — a role with more people
        shows more total SP without being overloaded per person. Provide
        headcount for the meaningful per-capita measure.

EXIT CODES:
    0 success ; 1 missing/unreadable file.
"""

import argparse
import csv
import math
import statistics
import sys

# ---- Thresholds ------------------------------------------------------------
FRAG_THRESHOLD = 2.0          # tickets / SP above this => over-fragmentation
OPS_RATIO_THRESHOLD = 0.50    # ops_sp / sp above this => silo risk
OPS_HEALTHY_LO = 0.25
OPS_HEALTHY_HI = 0.35
CORR_THRESHOLD = 0.10         # avg pairwise correlation below this => silo risk
CV_THRESHOLD = 0.50           # coefficient of variation above this => imbalance


def pearson(xs, ys):
    """Pearson correlation coefficient computed by hand (stdlib only).

    Returns None when undefined (fewer than 2 points, or zero variance in
    either series).
    """
    n = len(xs)
    if n < 2 or len(ys) != n:
        return None
    mean_x = statistics.fmean(xs)
    mean_y = statistics.fmean(ys)
    num = 0.0
    sx = 0.0
    sy = 0.0
    for x, y in zip(xs, ys):
        dx = x - mean_x
        dy = y - mean_y
        num += dx * dy
        sx += dx * dx
        sy += dy * dy
    denom = math.sqrt(sx * sy)
    if denom == 0:
        return None
    return num / denom


def load_rows(path):
    """Read the CSV, returning (rows, has_ops, has_head). Warns + skips bad rows."""
    try:
        f = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        sys.stderr.write("ERROR: file not found (파일 없음): %s\n" % path)
        sys.exit(1)
    except OSError as exc:
        sys.stderr.write("ERROR: cannot read file (읽기 실패): %s (%s)\n"
                         % (path, exc))
        sys.exit(1)

    rows = []
    with f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            sys.stderr.write("ERROR: empty CSV (빈 파일): %s\n" % path)
            sys.exit(1)
        cols = {c.strip().lower() for c in reader.fieldnames if c}
        required = {"role", "period", "sp", "tickets"}
        missing = required - cols
        if missing:
            sys.stderr.write(
                "ERROR: missing required columns (필수 열 누락): %s\n"
                % ", ".join(sorted(missing)))
            sys.exit(1)
        has_ops = "ops_sp" in cols
        if not has_ops:
            sys.stderr.write(
                "WARNING: no 'ops_sp' column — skipping ops-ratio analysis "
                "(ops_sp 열 없음 — 운영 비율 분석 생략).\n")
        has_head = "headcount" in cols
        if not has_head:
            sys.stderr.write(
                "WARNING: no 'headcount' column — workload imbalance falls back "
                "to RAW total SP, which is confounded by team size (a role with "
                "more people shows more total SP). Add 'headcount' for a per-capita "
                "(인당) measure (headcount 열 없음 — 불균형은 인원수에 영향받는 "
                "원시 SP 기준; per-capita 측정을 원하면 headcount 열 추가).\n")

        for lineno, raw in enumerate(reader, start=2):
            # Normalize keys to lowercase/stripped for robust access.
            r = {(k.strip().lower() if k else k): v for k, v in raw.items()}
            role = (r.get("role") or "").strip()
            period = (r.get("period") or "").strip()
            if not role or not period:
                sys.stderr.write(
                    "WARNING: line %d skipped — blank role/period.\n" % lineno)
                continue
            try:
                sp = float(r.get("sp"))
                tickets = float(r.get("tickets"))
            except (TypeError, ValueError):
                sys.stderr.write(
                    "WARNING: line %d skipped — bad sp/tickets value.\n"
                    % lineno)
                continue
            ops_sp = None
            if has_ops:
                val = (r.get("ops_sp") or "").strip()
                if val == "":
                    ops_sp = None
                else:
                    try:
                        ops_sp = float(val)
                    except ValueError:
                        sys.stderr.write(
                            "WARNING: line %d — bad ops_sp, treated as missing.\n"
                            % lineno)
                        ops_sp = None
            head = None
            if has_head:
                val = (r.get("headcount") or "").strip()
                if val != "":
                    try:
                        head = float(val)
                    except ValueError:
                        sys.stderr.write(
                            "WARNING: line %d — bad headcount, treated as missing.\n"
                            % lineno)
                        head = None
            rows.append({
                "role": role,
                "period": period,
                "sp": sp,
                "tickets": tickets,
                "ops_sp": ops_sp,
                "headcount": head,
            })

    if not rows:
        sys.stderr.write("ERROR: no valid data rows (유효 데이터 없음).\n")
        sys.exit(1)
    return rows, has_ops, has_head


def fmt(x, nd=2):
    if x is None:
        return "n/a"
    return ("%." + str(nd) + "f") % x


def analyze(rows, has_ops, has_head=False):
    roles = sorted({r["role"] for r in rows})
    periods = sorted({r["period"] for r in rows})

    # Per-role aggregates.
    per_role = {}
    for role in roles:
        rr = [r for r in rows if r["role"] == role]
        sp = sum(r["sp"] for r in rr)
        tickets = sum(r["tickets"] for r in rr)
        ops = sum(r["ops_sp"] for r in rr
                  if r["ops_sp"] is not None) if has_ops else None
        ops_known = any(r["ops_sp"] is not None for r in rr) if has_ops else False
        per_role[role] = {
            "sp": sp,
            "tickets": tickets,
            "ops": ops if ops_known else None,
            "frag": (tickets / sp) if sp > 0 else None,
            "ops_ratio": (ops / sp) if (ops_known and sp > 0) else None,
        }

    total_sp = sum(r["sp"] for r in rows)
    total_tickets = sum(r["tickets"] for r in rows)
    overall_frag = (total_tickets / total_sp) if total_sp > 0 else None

    total_ops = None
    overall_ops_ratio = None
    if has_ops:
        ops_vals = [r["ops_sp"] for r in rows if r["ops_sp"] is not None]
        if ops_vals:
            total_ops = sum(ops_vals)
            overall_ops_ratio = (total_ops / total_sp) if total_sp > 0 else None

    # Workload imbalance across roles.
    # Raw total SP is confounded by team size, so prefer a per-capita measure
    # when headcount is available: for each role, mean over periods of
    # (period SP / period headcount), then CV across roles. This matches how a
    # human analyst reads "is the load evenly distributed per person?".
    percap_by_role = None
    if has_head:
        percap_by_role = {}
        for role in roles:
            vals = []
            for p in periods:
                rr = [r for r in rows
                      if r["role"] == role and r["period"] == p]
                sp_p = sum(r["sp"] for r in rr)
                heads = [r["headcount"] for r in rr if r["headcount"]]
                head_p = max(heads) if heads else None
                if head_p:
                    vals.append(sp_p / head_p)
            percap_by_role[role] = statistics.fmean(vals) if vals else None

    if percap_by_role is not None and all(
            v is not None for v in percap_by_role.values()):
        imbalance_basis = "per-capita"
        imbalance_vals = [percap_by_role[role] for role in roles]
    else:
        imbalance_basis = "raw-total"
        imbalance_vals = [per_role[role]["sp"] for role in roles]
    mean_sp = statistics.fmean(imbalance_vals) if imbalance_vals else 0.0
    stdev_sp = statistics.stdev(imbalance_vals) if len(imbalance_vals) > 1 else 0.0
    cv = (stdev_sp / mean_sp) if mean_sp > 0 else None

    # Cross-role correlation: align each role's SP series by period.
    series = {}
    for role in roles:
        s = []
        for p in periods:
            vals = [r["sp"] for r in rows
                    if r["role"] == role and r["period"] == p]
            s.append(sum(vals) if vals else 0.0)
        series[role] = s

    pair_corrs = []
    pair_detail = []
    for i in range(len(roles)):
        for j in range(i + 1, len(roles)):
            a, b = roles[i], roles[j]
            c = pearson(series[a], series[b])
            pair_detail.append((a, b, c))
            if c is not None:
                pair_corrs.append(c)
    avg_corr = statistics.fmean(pair_corrs) if pair_corrs else None

    return {
        "roles": roles,
        "periods": periods,
        "per_role": per_role,
        "total_sp": total_sp,
        "total_tickets": total_tickets,
        "overall_frag": overall_frag,
        "total_ops": total_ops,
        "overall_ops_ratio": overall_ops_ratio,
        "mean_sp": mean_sp,
        "stdev_sp": stdev_sp,
        "cv": cv,
        "imbalance_basis": imbalance_basis,
        "percap_by_role": percap_by_role,
        "avg_corr": avg_corr,
        "pair_detail": pair_detail,
    }


def report(a, has_ops):
    out = []
    w = out.append
    flags = []

    w("=" * 70)
    w("WORKLOAD FRAGMENTATION REPORT (워크로드 파편화 리포트)")
    w("=" * 70)
    w("Roles (역할): %d   |   Periods (기간): %d"
      % (len(a["roles"]), len(a["periods"])))
    w("")

    # --- Workload imbalance ---
    w("-" * 70)
    w("1. WORKLOAD IMBALANCE ACROSS ROLES (역할 간 부하 불균형)")
    w("-" * 70)
    percap = a.get("percap_by_role")
    if a["imbalance_basis"] == "per-capita":
        w("  basis (기준): per-capita SP (인당 SP) — team-size adjusted")
        for role in a["roles"]:
            w("  %-12s per-capita SP (인당 SP): %s   [total %s]"
              % (role, fmt(percap[role]), fmt(a["per_role"][role]["sp"])))
    else:
        w("  basis (기준): RAW total SP (원시 총 SP) — NOT team-size adjusted; "
          "add 'headcount' for per-capita")
        for role in a["roles"]:
            w("  %-12s total SP (총 SP): %s"
              % (role, fmt(a["per_role"][role]["sp"])))
    w("  mean (평균): %s   STDEV (표준편차): %s"
      % (fmt(a["mean_sp"]), fmt(a["stdev_sp"])))
    cv = a["cv"]
    if cv is None:
        w("  coefficient of variation (변동계수): n/a")
    else:
        tag = "[high imbalance / 높은 불균형]" if cv > CV_THRESHOLD else "[balanced / 균형]"
        w("  coefficient of variation (변동계수): %s %s" % (fmt(cv), tag))
        if cv > CV_THRESHOLD:
            flags.append("IMBALANCE (불균형): CV %s > %s — stability beats "
                         "heroics (안정 > 영웅주의)." % (fmt(cv), fmt(CV_THRESHOLD, 1)))
    w("")

    # --- Fragmentation ---
    w("-" * 70)
    w("2. FRAGMENTATION INDEX = tickets / SP (파편화 지수)")
    w("-" * 70)
    over_frag_roles = []
    for role in a["roles"]:
        frag = a["per_role"][role]["frag"]
        if frag is None:
            w("  %-12s frag (파편화): n/a" % role)
            continue
        tag = "[over-fragmented / 과파편]" if frag > FRAG_THRESHOLD else "[ok]"
        w("  %-12s frag (파편화): %s %s" % (role, fmt(frag), tag))
        if frag > FRAG_THRESHOLD:
            over_frag_roles.append(role)
    of = a["overall_frag"]
    if of is None:
        w("  OVERALL frag (전체 파편화): n/a")
    else:
        tag = "[over-fragmented / 과파편]" if of > FRAG_THRESHOLD else "[ok]"
        w("  OVERALL frag (전체 파편화): %s %s" % (fmt(of), tag))
    if over_frag_roles or (of is not None and of > FRAG_THRESHOLD):
        who = ", ".join(over_frag_roles) if over_frag_roles else "overall"
        flags.append("OVER-FRAGMENTATION (과파편): %s above %s — "
                     "context-switching ~1/6 output loss (전환비용 ~1/6 손실)."
                     % (who, fmt(FRAG_THRESHOLD, 1)))
    w("")

    # --- Cross-role correlation ---
    w("-" * 70)
    w("3. CROSS-ROLE CORRELATION (역할 간 상관 — 공조층 신호)")
    w("-" * 70)
    for x, y, c in a["pair_detail"]:
        w("  %-12s <-> %-12s  r = %s" % (x, y, fmt(c)))
    ac = a["avg_corr"]
    if ac is None:
        w("  average pairwise correlation (평균 상관): n/a "
          "(need >=2 roles & variance)")
    else:
        tag = "[silo risk / 사일로 위험]" if ac < CORR_THRESHOLD else "[cooperating / 공조]"
        w("  average pairwise correlation (평균 상관): %s %s" % (fmt(ac), tag))
        if ac < CORR_THRESHOLD:
            flags.append("SILO RISK (사일로 위험): avg correlation %s < %s — "
                         "roles moving independently (독립적 움직임)."
                         % (fmt(ac), fmt(CORR_THRESHOLD, 2)))
    w("")

    # --- Operations ratio ---
    w("-" * 70)
    w("4. OPERATIONS RATIO = ops_sp / sp (운영 비율)")
    w("-" * 70)
    if not has_ops or a["overall_ops_ratio"] is None:
        w("  (skipped — no ops_sp data / ops_sp 데이터 없음으로 생략)")
    else:
        for role in a["roles"]:
            orr = a["per_role"][role]["ops_ratio"]
            if orr is None:
                w("  %-12s ops ratio (운영 비율): n/a" % role)
                continue
            if orr > OPS_RATIO_THRESHOLD:
                tag = "[silo risk / 사일로 위험]"
            elif OPS_HEALTHY_LO <= orr <= OPS_HEALTHY_HI:
                tag = "[healthy / 건강]"
            else:
                tag = "[watch / 주의]"
            w("  %-12s ops ratio (운영 비율): %s %s"
              % (role, fmt(orr), tag))
            if orr > OPS_RATIO_THRESHOLD:
                flags.append("SILO RISK (사일로 위험): %s ops ratio %s > 50%% — "
                             "pipeline fragments to each-for-themselves "
                             "(각자도생)." % (role, fmt(orr)))
        oor = a["overall_ops_ratio"]
        if oor > OPS_RATIO_THRESHOLD:
            tag = "[silo risk / 사일로 위험]"
        elif OPS_HEALTHY_LO <= oor <= OPS_HEALTHY_HI:
            tag = "[healthy / 건강]"
        else:
            tag = "[watch / 주의]"
        w("  OVERALL ops ratio (전체 운영 비율): %s %s" % (fmt(oor), tag))
        w("  healthy band (건강 구간): %d%%-%d%%"
          % (OPS_HEALTHY_LO * 100, OPS_HEALTHY_HI * 100))
    w("")

    # --- Flags summary ---
    w("=" * 70)
    w("FLAGS (위험 신호 요약)")
    w("=" * 70)
    if not flags:
        w("  None — workload is aligned & cooperative (모두 양호: 정렬·공조 상태).")
    else:
        for fl in flags:
            w("  [!] " + fl)
    w("=" * 70)

    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Workload distribution & fragmentation analyzer "
                    "(워크로드 분포·파편화 분석기). Surfaces over-fragmentation, "
                    "role silos, and workload imbalance from completed-work data.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="CSV columns (열): role, period, sp, tickets, ops_sp(optional).\n"
               "Thresholds: frag>2.0=over-fragmented; ops>50%=silo; "
               "avg corr<0.1=silo; CV>0.5=imbalance.",
    )
    parser.add_argument("csv_path", help="path to the workload CSV "
                                         "(워크로드 CSV 경로)")
    args = parser.parse_args(argv)

    rows, has_ops, has_head = load_rows(args.csv_path)
    a = analyze(rows, has_ops, has_head)
    print(report(a, has_ops))
    return 0


if __name__ == "__main__":
    sys.exit(main())
