#!/usr/bin/env python3
"""Monte Carlo flow forecaster — #NoEstimates from history (몬테카를로 예측기 — 추정 대신 흐름).

Part of the "aligned-delivery" skill. The capstone of the SP-free / #NoEstimates
line: it FORECASTS a completion date from your own **historical throughput**, not
from anyone's estimate. You feed it how many items you finished each past period
(the same SP-free 도/footprint flow_metrics.py reads) and a remaining backlog; it
runs a Monte Carlo simulation and answers "with X% confidence, you are done within
N periods". (추정이 아니라 과거 처리량 분포에서 완료 시점을 확률로 예측한다.)

WHY this, not estimates: estimates are guesses about the future; this resamples the
*actual* past. It does not ask the team to size anything — it reads what the system
already did and projects its own footprint (도) forward. Stability of throughput,
not heroic speed, is what makes the forecast tight (안정된 처리량 → 좁은 예측).

------------------------------------------------------------------------------
INPUT CSV COLUMNS (열 이름) — one row per HISTORICAL period:
    throughput : completed items in that period (count). REQUIRED. Non-numeric or
                 blank cells are skipped with a warning.
    period     : a label for the period (e.g. 2026-01 or a sprint id). OPTIONAL —
                 only used to echo how much history was read; not needed to forecast.

METHOD (방법) — bootstrap Monte Carlo:
    For each simulation, repeatedly draw a past period's throughput AT RANDOM WITH
    REPLACEMENT (bootstrap) and accumulate the items, counting periods, until the
    running sum >= backlog. That count is one sampled "periods-to-complete". Across
    many simulations this builds the distribution; we report its percentiles.
    (각 시뮬레이션: 과거 처리량을 복원추출로 누적해 backlog 도달까지 걸린 기간 수를 셈.
    이를 수천 번 반복해 분포의 백분위수를 보고.)

OUTPUT (출력) — bilingual percentiles of periods-to-complete:
    P50  — coin-flip (50% 확률로 이 안에 완료)
    P85  — a common planning confidence (85% 확률)
    P95  — conservative (95% 확률)
    A higher percentile = MORE periods = MORE confidence it is done by then.

CAVEATS (주의) — read these, this is a forecast not a promise:
    • It assumes the PAST throughput distribution still holds (team, scope, process
      unchanged). A reorg, a scope blow-up, or a new domain breaks that assumption.
      (과거 분포가 유지된다는 가정 — 조직·범위·프로세스가 바뀌면 깨짐.)
    • It needs ENOUGH history. With < ~6 periods the distribution is too thin to
      trust; the script warns and still runs, but read the result loosely.
      (이력이 6기간 미만이면 신뢰 어려움 — 경고 후 실행하되 느슨하게 읽을 것.)
    • Zeros are kept (a period of zero delivery is real signal). If EVERY period is
      zero, the backlog can never complete and the script errors out.

SAMPLE CSV (샘플):
    period,throughput
    2026-W01,6
    2026-W02,9
    2026-W03,4
    2026-W04,7
    2026-W05,8
    2026-W06,5

USAGE (사용법):
    python3 forecast_montecarlo.py sample_throughput.csv --backlog 50
    python3 forecast_montecarlo.py sample_throughput.csv --backlog 50 --simulations 20000 --seed 7
    python3 forecast_montecarlo.py --help

EXIT CODES:
    0 success ; 1 missing/unreadable file, missing 'throughput' column, no usable
      numeric rows, all-zero throughput, or a non-positive backlog.
"""

import argparse
import csv
import statistics
import sys
import random

MIN_HISTORY = 6           # warn (don't fail) below this many periods (prior)
DEFAULT_SIMS = 10000
DEFAULT_SEED = 42         # fixed for reproducibility (use random.Random(seed))


def load_throughput(path):
    """Read the CSV → list of (period_label, throughput_float). Warns + skips bad cells."""
    try:
        f = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        sys.stderr.write("ERROR: file not found (파일 없음): %s\n" % path)
        sys.exit(1)
    except OSError as exc:
        sys.stderr.write("ERROR: cannot read file (읽기 실패): %s (%s)\n" % (path, exc))
        sys.exit(1)

    history = []
    with f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            sys.stderr.write("ERROR: empty CSV (빈 파일): %s\n" % path)
            sys.exit(1)
        cols = {c.strip().lower() for c in reader.fieldnames if c}
        if "throughput" not in cols:
            sys.stderr.write(
                "ERROR: missing required column 'throughput' (필수 열 누락: throughput).\n")
            sys.exit(1)
        has_period = "period" in cols

        for lineno, raw in enumerate(reader, start=2):
            r = {(k.strip().lower() if k else k): v for k, v in raw.items()}
            cell = (r.get("throughput") or "").strip()
            if not cell:
                sys.stderr.write("WARNING: line %d skipped — blank throughput.\n" % lineno)
                continue
            try:
                val = float(cell)
            except ValueError:
                sys.stderr.write(
                    "WARNING: line %d skipped — non-numeric throughput %r "
                    "(숫자 아님).\n" % (lineno, cell))
                continue
            if val < 0:
                sys.stderr.write(
                    "WARNING: line %d skipped — negative throughput %s "
                    "(음수).\n" % (lineno, cell))
                continue
            label = (r.get("period") or "").strip() if has_period else ""
            history.append((label, val))

    if not history:
        sys.stderr.write("ERROR: no usable numeric throughput rows (유효 처리량 없음).\n")
        sys.exit(1)
    return history


def simulate(throughputs, backlog, simulations, seed):
    """Bootstrap Monte Carlo → sorted list of periods-to-complete (one per simulation)."""
    rng = random.Random(seed)
    results = []
    pick = rng.choice
    for _ in range(simulations):
        done = 0.0
        periods = 0
        # cap guards against pathological draws (mostly-zero history); generous.
        while done < backlog:
            done += pick(throughputs)
            periods += 1
        results.append(periods)
    results.sort()
    return results


def percentile(sorted_vals, pct):
    """Nearest-rank percentile (conservative, integer-friendly) on a SORTED list."""
    if not sorted_vals:
        return None
    import math
    rank = math.ceil(pct / 100.0 * len(sorted_vals))
    rank = max(1, min(rank, len(sorted_vals)))
    return sorted_vals[rank - 1]


def fmt(x, nd=1):
    if x is None:
        return "n/a"
    return ("%." + str(nd) + "f") % x


def report(history, results, backlog, simulations, seed):
    out = []
    w = out.append
    vals = [v for _, v in history]
    n = len(vals)
    mean = statistics.fmean(vals)
    stdev = statistics.stdev(vals) if n > 1 else 0.0
    cv = (stdev / mean) if mean > 0 else None

    p50 = percentile(results, 50)
    p85 = percentile(results, 85)
    p95 = percentile(results, 95)

    w("=" * 70)
    w("MONTE CARLO FORECAST (몬테카를로 예측) — from history, not estimates (추정 아님)")
    w("=" * 70)
    w("Backlog to complete (남은 백로그): %d items   |   simulations (시뮬레이션): %d"
      % (backlog, simulations))
    w("History periods (이력 기간 수): %d   |   seed (시드, 재현용): %d" % (n, seed))
    w("")

    # --- History summary ---
    w("-" * 70)
    w("HISTORICAL THROUGHPUT (과거 처리량) — the sampled distribution (표본 분포)")
    w("-" * 70)
    w("  values (값): %s" % ", ".join(fmt(v, 0) for v in vals))
    w("  mean/period (기간 평균): %s   STDEV (표준편차): %s   CV (변동계수): %s"
      % (fmt(mean), fmt(stdev), fmt(cv, 2) if cv is not None else "n/a"))
    if n < MIN_HISTORY:
        w("  [!] only %d periods (< %d) — thin history, read the forecast LOOSELY "
          "(이력 %d기간 < %d — 느슨하게 해석)." % (n, MIN_HISTORY, n, MIN_HISTORY))
    w("")

    # --- Forecast ---
    w("-" * 70)
    w("FORECAST: periods to complete the backlog (완료까지 기간 — 확률별)")
    w("-" * 70)
    w("  (higher percentile = more periods = more confidence / 높은 백분위 = 더 많은 기간 = 더 확실)")
    w("  P50 (50%% 확률): %d periods (기간)" % p50)
    w("  P85 (85%% 확률): %d periods (기간)" % p85)
    w("  P95 (95%% 확률): %d periods (기간)" % p95)
    w("")
    w("  READ (해석): 85%% confidence — done within %d periods. "
      "(85%% 확신 — %d기간 안에 완료.)" % (p85, p85))
    w("  This forecasts FROM your own throughput history, not from estimates "
      "(추정이 아니라 과거 처리량에서 예측).")
    w("")

    # --- Caveats ---
    w("=" * 70)
    w("CAVEATS (주의)")
    w("=" * 70)
    w("  • Assumes the past throughput distribution still holds — a reorg / scope")
    w("    blow-up / new domain breaks it (과거 분포 유지 가정 — 변화 시 깨짐).")
    if n < MIN_HISTORY:
        w("  • Thin history (%d < %d periods): treat the numbers as direction, not a "
          "promise (이력 부족 — 약속 아닌 방향)." % (n, MIN_HISTORY))
    w("  • A forecast, not a commitment; re-run as new periods land "
      "(예측이지 약속 아님 — 기간이 쌓이면 재실행).")
    w("=" * 70)
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Monte Carlo flow forecaster (몬테카를로 예측기) — probabilistic "
                    "completion forecast from historical throughput, the #NoEstimates "
                    "way. Resamples your own past, asks no one to estimate.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="CSV columns (열): throughput(required, count), period(optional label).\n"
               "Bootstrap: sample past throughput with replacement until backlog met; "
               "report P50/P85/P95 periods-to-complete. Forecast, not a promise.",
    )
    parser.add_argument("csv_path", help="path to the throughput history CSV (처리량 이력 CSV)")
    parser.add_argument("--backlog", type=int, required=True,
                        help="remaining items to forecast (남은 작업 수) — required, > 0")
    parser.add_argument("--simulations", type=int, default=DEFAULT_SIMS,
                        help="number of Monte Carlo runs (시뮬레이션 횟수, 기본 %d)" % DEFAULT_SIMS)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED,
                        help="RNG seed for reproducibility (재현용 시드, 기본 %d)" % DEFAULT_SEED)
    args = parser.parse_args(argv)

    if args.backlog <= 0:
        sys.stderr.write("ERROR: --backlog must be > 0 (백로그는 0보다 커야 함).\n")
        sys.exit(1)
    if args.simulations <= 0:
        sys.stderr.write("ERROR: --simulations must be > 0 (시뮬레이션 횟수는 0보다 커야 함).\n")
        sys.exit(1)

    history = load_throughput(args.csv_path)
    throughputs = [v for _, v in history]
    if all(v == 0 for v in throughputs):
        sys.stderr.write(
            "ERROR: every period has zero throughput — backlog can never complete "
            "(모든 기간 처리량 0 — 완료 불가).\n")
        sys.exit(1)

    results = simulate(throughputs, args.backlog, args.simulations, args.seed)
    print(report(history, results, args.backlog, args.simulations, args.seed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
