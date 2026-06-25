#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Team health-check analyzer (팀 헬스체크 분석기).

Part of the "aligned-delivery" skill. A team health check has a QUANTITATIVE
survey (1-5 scale, per metric, per period) plus a qualitative 1:1 "correction"
step. Survey scores alone OVER-REPORT, so this script produces a worksheet that
reconciles the numbers against the positive/negative wording you collect in 1:1s,
recovering the true 기 (operating state).

The lenses behind this skill:
  - 리 (latent structure)
  - 기 (operating state — read via health checks and 1:1s)
  - 도 (measurable footprint)

------------------------------------------------------------------------------
ACCEPTED CSV FORMATS (두 가지 형식 지원)
------------------------------------------------------------------------------

1) TIDY / LONG (default, 기본):
   one row per question per period (per respondent or already-averaged).

       question,period,score
       팀 만족도,25.2H,4.1
       팀 만족도,26.01,3.8
       커뮤니케이션 진솔함,25.2H,3.4
       커뮤니케이션 진솔함,26.01,3.6

2) WIDE (넓은 형식):
   first column is `period` (or `시점`); every other column is a question.

       period,팀 만족도,커뮤니케이션 진솔함,업무 만족도
       25.2H,4.1,3.4,3.9
       26.01,3.8,3.6,4.2

The format is auto-detected from the header row.

------------------------------------------------------------------------------
USAGE (사용법)
------------------------------------------------------------------------------

    python3 health_check_analyze.py sample_health_check.csv
    python3 health_check_analyze.py data.csv --green 4.0 --red 3.0 --scale 5
    python3 health_check_analyze.py --help

Exit code 0 on success; 1 if the file is missing/unreadable.
"""

import argparse
import csv
import statistics
import sys


# ----------------------------------------------------------------------------
# Parsing
# ----------------------------------------------------------------------------

def _to_float(raw):
    """Parse a score; return None if it can't be parsed."""
    if raw is None:
        return None
    s = str(raw).strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _norm(name):
    return (name or "").strip().lower()


def detect_and_read(path):
    """Read the CSV and return a dict: {question: {period: [scores...]}}.

    Auto-detects tidy/long vs wide layout. Warns (to stderr) and skips rows
    with missing columns or unparseable scores instead of crashing.
    """
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = [r for r in reader if any(cell.strip() for cell in r)]

    if not rows:
        print("Warning (경고): file is empty — no rows to analyze.", file=sys.stderr)
        return {}

    header = [h.strip() for h in rows[0]]
    norm_header = [_norm(h) for h in header]

    # Decide format. Tidy/long requires question + period + score columns.
    long_cols = {"question", "period", "score"}
    is_long = long_cols.issubset(set(norm_header))

    data = {}

    if is_long:
        qi = norm_header.index("question")
        pi = norm_header.index("period")
        si = norm_header.index("score")
        for lineno, r in enumerate(rows[1:], start=2):
            if max(qi, pi, si) >= len(r):
                print("Warning (경고): line %d has missing columns — skipped."
                      % lineno, file=sys.stderr)
                continue
            question = r[qi].strip()
            period = r[pi].strip()
            score = _to_float(r[si])
            if not question or not period:
                print("Warning (경고): line %d missing question/period — skipped."
                      % lineno, file=sys.stderr)
                continue
            if score is None:
                print("Warning (경고): line %d has unparseable score %r — skipped."
                      % (lineno, r[si]), file=sys.stderr)
                continue
            data.setdefault(question, {}).setdefault(period, []).append(score)
    else:
        # Wide format: first column = period/시점, rest = questions.
        first = norm_header[0]
        if first not in ("period", "시점"):
            print("Warning (경고): first column %r is not 'period'/'시점'; "
                  "treating it as the period column anyway." % header[0],
                  file=sys.stderr)
        questions = header[1:]
        for lineno, r in enumerate(rows[1:], start=2):
            if len(r) < 1 or not r[0].strip():
                print("Warning (경고): line %d missing period — skipped."
                      % lineno, file=sys.stderr)
                continue
            period = r[0].strip()
            for col, question in enumerate(questions, start=1):
                if not question:
                    continue
                if col >= len(r):
                    continue
                score = _to_float(r[col])
                if score is None:
                    if str(r[col]).strip() != "":
                        print("Warning (경고): line %d, column %r unparseable "
                              "score %r — skipped." % (lineno, question, r[col]),
                              file=sys.stderr)
                    continue
                data.setdefault(question, {}).setdefault(period, []).append(score)

    return data


# ----------------------------------------------------------------------------
# Analysis
# ----------------------------------------------------------------------------

def flag_for(avg, green, red):
    if avg >= green:
        return "GREEN"
    if avg >= red:
        return "AMBER"
    return "RED"


def ordered_periods(data):
    """All periods across all questions, in first-seen then sorted order."""
    periods = set()
    for pmap in data.values():
        periods.update(pmap.keys())
    return sorted(periods)


def analyze(data, green, red):
    """Return a per-question summary list."""
    periods = ordered_periods(data)
    results = []
    for question, pmap in data.items():
        all_scores = [s for scores in pmap.values() for s in scores]
        if not all_scores:
            continue
        overall_avg = statistics.fmean(all_scores)
        # Dispersion: prefer across all raw scores; need >=2 points.
        stdev = statistics.pstdev(all_scores) if len(all_scores) >= 2 else None

        per_period = {}
        for p in periods:
            if p in pmap and pmap[p]:
                per_period[p] = statistics.fmean(pmap[p])

        present = [p for p in periods if p in per_period]
        delta = None
        delta_from = delta_to = None
        if len(present) >= 2:
            delta_from, delta_to = present[-2], present[-1]
            delta = per_period[delta_to] - per_period[delta_from]

        results.append({
            "question": question,
            "avg": overall_avg,
            "stdev": stdev,
            "per_period": per_period,
            "present_periods": present,
            "delta": delta,
            "delta_from": delta_from,
            "delta_to": delta_to,
            "flag": flag_for(overall_avg, green, red),
        })
    # Sort by flag severity then ascending avg so the worst float to the top.
    sev = {"RED": 0, "AMBER": 1, "GREEN": 2}
    results.sort(key=lambda r: (sev[r["flag"]], r["avg"]))
    return results, periods


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------

def _display_width(s):
    """Approximate display width treating CJK as width 2."""
    w = 0
    for ch in s:
        o = ord(ch)
        if (0x1100 <= o <= 0x115F or 0x2E80 <= o <= 0x303E or
                0x3041 <= o <= 0x33FF or 0x3400 <= o <= 0x4DBF or
                0x4E00 <= o <= 0x9FFF or 0xA000 <= o <= 0xA4CF or
                0xAC00 <= o <= 0xD7A3 or 0xF900 <= o <= 0xFAFF or
                0xFE30 <= o <= 0xFE4F or 0xFF00 <= o <= 0xFF60 or
                0xFFE0 <= o <= 0xFFE6):
            w += 2
        else:
            w += 1
    return w


def _pad(s, width):
    s = str(s)
    pad = width - _display_width(s)
    return s + " " * max(0, pad)


def fmt_delta(d):
    if d is None:
        return "    n/a"
    sign = "+" if d >= 0 else "-"
    return "%s%.2f" % (sign, abs(d))


def print_report(results, periods, scale, green, red):
    print("=" * 78)
    print("TEAM HEALTH CHECK — ANALYSIS (팀 헬스체크 분석)")
    print("=" * 78)
    print("Scale (척도): 1-%g   Green (양호) >= %.1f   "
          "Amber (주의) %.1f-%.1f   Red (위험) < %.1f"
          % (scale, green, red, green, red))
    print("Periods (시점): %s" % (", ".join(periods) if periods else "(none)"))
    print()

    if not results:
        print("No analyzable data found (분석할 데이터가 없습니다).")
        return

    # Quantitative summary table.
    cols = [
        ("Question (지표)", 34),
        ("Avg (평균)", 10),
        ("Stdev (편차)", 12),
        ("Δ (변화)", 9),
        ("Flag (신호)", 12),
    ]
    header = "  ".join(_pad(name, w) for name, w in cols)
    print(header)
    print("-" * _display_width(header))

    for r in results:
        avg = "%.2f" % r["avg"]
        stdev = "%.2f" % r["stdev"] if r["stdev"] is not None else "n/a"
        delta = fmt_delta(r["delta"])
        flag = r["flag"]
        # Annotate a drop even when still green.
        note = ""
        if r["delta"] is not None and r["delta"] < 0:
            note = " ↓drop(하락)"
        hi_disp = ""
        if r["stdev"] is not None and r["stdev"] >= 0.75:
            hi_disp = " ⚠hidden-disagree(잠재이견)"
        line = "  ".join([
            _pad(r["question"], cols[0][1]),
            _pad(avg, cols[1][1]),
            _pad(stdev, cols[2][1]),
            _pad(delta, cols[3][1]),
            _pad(flag + note, cols[4][1]),
        ]) + hi_disp
        print(line)

    print()
    # Per-period detail when multiple periods exist.
    if len(periods) >= 2:
        print("PER-PERIOD AVERAGES (시점별 평균)")
        print("-" * 40)
        head = _pad("Question (지표)", 34) + "  " + "  ".join(_pad(p, 8) for p in periods)
        print(head)
        for r in sorted(results, key=lambda x: x["question"]):
            cells = []
            for p in periods:
                v = r["per_period"].get(p)
                cells.append(_pad("%.2f" % v if v is not None else "-", 8))
            print(_pad(r["question"], 34) + "  " + "  ".join(cells))
        print()

    # Attention callouts.
    drops = [r for r in results if r["delta"] is not None and r["delta"] < 0]
    reds = [r for r in results if r["flag"] == "RED"]
    ambers = [r for r in results if r["flag"] == "AMBER"]
    if reds or ambers or drops:
        print("ATTENTION (주의 신호)")
        print("-" * 40)
        for r in reds:
            print("  [RED]   %s — avg %.2f below %.1f (위험)"
                  % (r["question"], r["avg"], red))
        for r in ambers:
            print("  [AMBER] %s — avg %.2f (주의)" % (r["question"], r["avg"]))
        for r in drops:
            print("  [DROP]  %s — %s→%s %s (하락; 양호해 보여도 점검)"
                  % (r["question"], r["delta_from"], r["delta_to"],
                     fmt_delta(r["delta"])))
        print()

    print_correction_worksheet(results)


def print_correction_worksheet(results):
    print("=" * 78)
    print("1:1 CORRECTION WORKSHEET (1:1 보정 워크시트)")
    print("=" * 78)
    print("Why (왜): survey scores OVER-REPORT. Reconcile each number against the "
          "positive/")
    print("negative wording from 1:1s to recover the true 기 (operating state).")
    print("(설문 점수는 과대보고됩니다. 1:1에서 들은 긍정/부정 표현과 대조해 "
          "실제 기(상태)를 보정하세요.)")
    print()

    cols = [
        ("Question (지표)", 30),
        ("Survey (점수)", 13),
        ("1:1 positive (긍정 표현)", 26),
        ("1:1 negative (부정 표현)", 26),
        ("Corrected read (보정 판단)", 26),
    ]
    header = " | ".join(_pad(name, w) for name, w in cols)
    print(header)
    print("-" * _display_width(header))
    for r in results:
        survey = "%.2f %s" % (r["avg"], r["flag"][:1])
        row = " | ".join([
            _pad(r["question"], cols[0][1]),
            _pad(survey, cols[1][1]),
            _pad("", cols[2][1]),
            _pad("", cols[3][1]),
            _pad("", cols[4][1]),
        ])
        print(row)
    print()
    print("Fill the blank cells during 1:1s, then set the corrected read.")
    print("(1:1 중 빈칸을 채운 뒤 보정 판단을 기입하세요.)")


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        prog="health_check_analyze.py",
        description=(
            "Analyze a team health-check survey (팀 헬스체크 설문 분석): "
            "per-question averages, stdev (dispersion / hidden disagreement), "
            "period-over-period deltas, and Green/Amber/Red flags — then emit a "
            "1:1 'correction' worksheet to reconcile over-reporting survey "
            "scores against 1:1 wording and recover the true 기 (operating state)."
        ),
        epilog=(
            "Accepts tidy/long (question,period,score) or wide "
            "(period,<question cols...>) CSV; format is auto-detected."
        ),
    )
    p.add_argument("csv_path", help="Path to the survey CSV (설문 CSV 경로).")
    p.add_argument("--scale", type=float, default=5.0,
                   help="Top of the rating scale (척도 최대값). Default 5.")
    p.add_argument("--green", type=float, default=4.0,
                   help="Green threshold: avg >= this is healthy (양호 기준). "
                        "Default 4.0.")
    p.add_argument("--red", type=float, default=3.0,
                   help="Red threshold: avg < this is at-risk (위험 기준). "
                        "Default 3.0.")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.red > args.green:
        print("Warning (경고): --red (%.1f) > --green (%.1f); thresholds look "
              "swapped." % (args.red, args.green), file=sys.stderr)

    try:
        data = detect_and_read(args.csv_path)
    except FileNotFoundError:
        print("Error (오류): file not found: %s" % args.csv_path, file=sys.stderr)
        return 1
    except (OSError, IOError) as e:
        print("Error (오류): cannot read %s: %s" % (args.csv_path, e),
              file=sys.stderr)
        return 1

    results, periods = analyze(data, args.green, args.red)
    print_report(results, periods, args.scale, args.green, args.red)
    return 0


if __name__ == "__main__":
    sys.exit(main())
