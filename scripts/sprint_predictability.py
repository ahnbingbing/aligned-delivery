#!/usr/bin/env python3
"""sprint_predictability.py — Sprint predictability report (stdlib only).

Reads a sprint CSV and reports scope & completion predictability, workload
volatility (STDEV), and RAG (Red/Amber/Green) flags. Predictability is treated
as THE leading indicator of sustainable productivity: high output on broken
predictability is debt ("fake productivity"), not health.

Part of the "aligned-delivery" skill (리·기·도 / Do — the measurable footprint).

CSV format
----------
Exact column names (header row required):

    sprint,planned_sp,added_sp,completed_sp

Tiny sample CSV:

    sprint,planned_sp,added_sp,completed_sp
    S1,40,2,38
    S2,38,12,41
    S3,42,3,40

Usage
-----
    python3 sprint_predictability.py path/to/sprints.csv

Definitions
-----------
    scope predictability %      = planned / (planned + added) * 100
        (lower => more scope crept in mid-sprint; added_sp may be NEGATIVE
         when scope was trimmed mid-sprint, which pushes scope% above 100%)
    completion predictability % = completed / planned * 100
    workload STDEV              = population stdev of completed_sp
        (a debt / volatility signal — heroics and starvation both show here)

RAG rule
--------
    >= 90%  Green (G)
    75-90%  Amber (A)
    <  75%  Red   (R)
"""

import argparse
import csv
import statistics
import sys

# RAG thresholds (percent).
GREEN_MIN = 90.0
AMBER_MIN = 75.0

REQUIRED_COLUMNS = ["sprint", "planned_sp", "added_sp", "completed_sp"]


def rag_flag(pct):
    """Return single-letter RAG flag for a predictability percentage."""
    if pct is None:
        return "-"
    if pct >= GREEN_MIN:
        return "G"
    if pct >= AMBER_MIN:
        return "A"
    return "R"


def safe_pct(numerator, denominator):
    """Percentage that tolerates a non-positive/None denominator.

    A non-positive denominator (e.g. planned + added <= 0 after a large
    mid-sprint scope cut) is degenerate, so return None ("n/a") rather than a
    misleading negative percentage. Scope% above 100% is valid and means net
    scope was *removed* mid-sprint (no creep).
    """
    if denominator is None or denominator <= 0:
        return None
    return numerator / denominator * 100.0


def fmt_pct(pct):
    return "  n/a" if pct is None else "{:5.1f}%".format(pct)


def parse_rows(reader, warn):
    """Parse CSV rows into clean records, warning on and skipping bad rows."""
    records = []
    fieldnames = reader.fieldnames or []

    missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
    if missing:
        warn("missing expected column(s): {}".format(", ".join(missing)))
    extra = [c for c in fieldnames if c not in REQUIRED_COLUMNS]
    if extra:
        warn("ignoring extra column(s): {}".format(", ".join(extra)))

    for i, row in enumerate(reader, start=2):  # row 1 is the header
        name = (row.get("sprint") or "").strip() or "sprint@line{}".format(i)
        try:
            planned = float(row["planned_sp"])
            added = float(row["added_sp"])
            completed = float(row["completed_sp"])
        except (KeyError, TypeError, ValueError):
            warn("skipping row {} ({}): unparseable/missing numeric value".format(i, name))
            continue
        # added_sp may be negative: mid-sprint scope *reduction* (trimming) is
        # legitimate and a sign of discipline, not bad data. Only planned and
        # completed must be non-negative.
        if planned < 0 or completed < 0:
            warn("skipping row {} ({}): negative planned/completed".format(i, name))
            continue
        records.append({
            "sprint": name,
            "planned": planned,
            "added": added,
            "completed": completed,
        })
    return records


def build_report(records):
    """Return the full bilingual report text for the parsed records."""
    lines = []

    lines.append("=" * 72)
    lines.append("Sprint predictability report (스프린트 예측도 리포트)")
    lines.append("Do (도) — the measurable footprint (측정된 발자취)")
    lines.append("=" * 72)
    lines.append("")

    # Per-sprint table.
    header = "{:<16}{:>9}{:>8}{:>10}  {:>10} {:<3}  {:>10} {:<3}".format(
        "sprint", "planned", "added", "completed",
        "scope%", "", "compl%", "")
    lines.append(header)
    lines.append("-" * len(header))

    for r in records:
        scope = safe_pct(r["planned"], r["planned"] + r["added"])
        compl = safe_pct(r["completed"], r["planned"])
        lines.append("{:<16}{:>9.0f}{:>8.0f}{:>10.0f}  {:>10} {:<3}  {:>10} {:<3}".format(
            r["sprint"], r["planned"], r["added"], r["completed"],
            fmt_pct(scope), "[" + rag_flag(scope) + "]",
            fmt_pct(compl), "[" + rag_flag(compl) + "]"))

    lines.append("")

    # Overall aggregates.
    total_planned = sum(r["planned"] for r in records)
    total_added = sum(r["added"] for r in records)
    total_completed = sum(r["completed"] for r in records)
    completed_series = [r["completed"] for r in records]

    overall_scope = safe_pct(total_planned, total_planned + total_added)
    overall_compl = safe_pct(total_completed, total_planned)

    if len(completed_series) >= 2:
        workload_stdev = statistics.pstdev(completed_series)
    else:
        workload_stdev = 0.0
    mean_completed = statistics.fmean(completed_series) if completed_series else 0.0

    lines.append("-" * 72)
    lines.append("OVERALL (전체)")
    lines.append("-" * 72)
    lines.append("Scope predictability (스코프 예측도):      {} [{}]".format(
        fmt_pct(overall_scope), rag_flag(overall_scope)))
    lines.append("    planned / (planned + added) — lower = more mid-sprint scope creep")
    lines.append("    (낮을수록 스프린트 중 스코프가 더 끼어들었다는 신호)")
    lines.append("")
    lines.append("Completion predictability (완료 예측도):   {} [{}]".format(
        fmt_pct(overall_compl), rag_flag(overall_compl)))
    lines.append("    completed / planned")
    lines.append("")
    lines.append("Workload STDEV (워크로드 표준편차):        {:6.1f} SP".format(workload_stdev))
    lines.append("    over completed_sp (mean {:.1f}) — volatility = debt / 변동성은 곧 부채".format(
        mean_completed))
    lines.append("    heroic spikes and starvation both surface here (영웅적 과부하·기아 신호)")
    lines.append("")

    # Overall flag = the weaker of the two predictability signals.
    flags = [f for f in (rag_flag(overall_scope), rag_flag(overall_compl)) if f != "-"]
    order = {"R": 0, "A": 1, "G": 2}
    overall_flag = min(flags, key=lambda f: order[f]) if flags else "-"
    label = {"G": "Green (그린)", "A": "Amber (앰버)", "R": "Red (레드)", "-": "n/a"}[overall_flag]
    lines.append("OVERALL FLAG (종합 신호): [{}] {}".format(overall_flag, label))
    lines.append("=" * 72)
    lines.append("")

    # Interpretation hook (brief — the skill model does the deep reading).
    lines.append("Predictability is the leading indicator; velocity is lagging.")
    lines.append("High output on broken predictability is fake productivity — debt, not health.")
    lines.append("예측도가 선행지표이고 속도는 후행지표입니다.")
    lines.append("예측도가 깨진 채 나오는 높은 산출량은 가짜 생산성, 즉 부채입니다.")

    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="sprint_predictability.py",
        description=(
            "Report sprint scope & completion predictability, workload volatility "
            "(STDEV), and RAG flags from a sprint CSV. Predictability is treated as "
            "THE leading indicator of sustainable productivity. "
            "Expected columns: sprint, planned_sp, added_sp, completed_sp."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "RAG: >=90% Green (G) | 75-90% Amber (A) | <75% Red (R).\n"
            "Example:\n"
            "  python3 sprint_predictability.py sprints.csv"
        ),
    )
    parser.add_argument(
        "csv_path",
        help="Path to the sprint CSV (columns: sprint,planned_sp,added_sp,completed_sp)",
    )
    args = parser.parse_args(argv)

    def warn(msg):
        print("warning: {}".format(msg), file=sys.stderr)

    try:
        f = open(args.csv_path, newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        print("error: file not found: {}".format(args.csv_path), file=sys.stderr)
        return 1
    except OSError as exc:
        print("error: cannot open {}: {}".format(args.csv_path, exc), file=sys.stderr)
        return 1

    with f:
        reader = csv.DictReader(f)
        records = parse_rows(reader, warn)

    if not records:
        print("error: no usable rows found in {}".format(args.csv_path), file=sys.stderr)
        return 1

    print(build_report(records))
    return 0


if __name__ == "__main__":
    sys.exit(main())
