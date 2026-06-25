# Team Health Check Template (팀 헬스체크 템플릿)

Reads the **기 (operating state)** layer — the live operating state. Run it on a half-yearly loop
(or any time the wave feels off). The survey is the *prompt*, not the verdict: scores over-report,
so always pair it with the 1:1 **correction** below. (살아있는 운영 상태인 **기** 를 읽는다.
반기 루프마다, 혹은 파동이 이상할 때 돌려라. 설문은 *질문*이지 판정이 아니다 — 점수는
과대보고되므로 아래 1:1 **보정**과 반드시 함께.)

---

## Part 1 — Quantitative survey (정량 설문)

Score each statement **1–5** (1 = strongly disagree, 5 = strongly agree). Collect anonymously,
per period. (각 문항을 **1–5** 로 채점. 익명, 기간별 수집.)

| # | Metric (지표) | Statement (문항) | Score (1–5) |
|---|---|---|---|
| 1 | Team satisfaction (팀 만족도) | I want to keep working with my current teammates. (나는 현재의 팀원들과 계속 함께 일하고 싶다.) | |
| 2 | Way-of-working satisfaction (팀 일하는 방식 만족도) | I'm satisfied with how our team works. (나는 우리 팀의 일하는 방식에 만족한다.) | |
| 3 | Work-management ability (팀 업무 관리 능력) | I think our team manages work well. (나는 우리 팀의 업무 관리 능력이 좋다고 생각한다.) | |
| 4 | Communication candor (커뮤니케이션 진솔함) | I can share my opinions/thoughts candidly with teammates. (나는 내 의견·생각을 팀원에게 진솔하게 말할 수 있다.) | |
| 5 | Mistake/unknown sharing (실수/모름 공유 정도) | I can admit a mistake or "I don't know" to the team. (나는 팀에 나의 실수 혹은 모름을 공유할 수 있다.) | |
| 6 | Individual motivation (개인 동기부여) | I feel highly motivated in my current work. (나는 현재 업무에 대한 동기부여가 높다.) | |
| 7 | Independence (독립성향) | I work by priorities I set myself. (나는 내 스스로 정한 우선순위에 따라 일한다.) | |
| 8 | Conflict convergence (Conflict 수렴도) | In team meetings we converge differing opinions well. (나는 팀 전체 회의에서 서로 다른 의견을 잘 수렴한다.) | |
| 9 | Change acceptance (변화 수용도) | I'm okay with the process of adjusting how we work. (나는 일하는 방식을 맞춰가는 과정이 괜찮다.) | |
| 10 | Work satisfaction (업무 만족도) | I'm satisfied with my current work area. (나는 현재의 업무 분야에 만족한다.) | |

→ Enter results into `scripts/health_check_analyze.py` (tidy format: `question,period,score`,
or wide format: `period,<metric columns>`) for averages, STDEV, period-over-period deltas, and
Amber/Green flags. (결과를 `health_check_analyze.py`에 넣어 평균·표준편차·델타·플래그를 산출.)

**Flag legend (플래그):** Green ≥ 4.0 · Amber 3.0–4.0 · Red < 3.0 (1–5 scale). Also attend to any
metric that **dropped** period-over-period even if still Green, and to **high-STDEV** metrics
(hidden disagreement). (초록이어도 **하락한** 지표, **표준편차 높은**(숨은 이견) 지표에 주의.)

---

## Part 2 — 1:1 "correction" worksheet (1:1 "보정" 워크시트)

**Why (왜):** survey scores over-report. Reconcile each score against the positive/negative
**wording** people actually use in 1:1s to recover the true operating state (기). (설문 점수는
과대보고된다. 각 점수를 1:1에서 실제로 쓰는 긍정/부정 **표현**과 대조해 진짜 운영 상태(기)를
복원하라.)

| Metric (지표) | Survey score (설문 점수) | 1:1 positive wording (긍정 표현) | 1:1 negative wording (부정 표현) | Corrected read (보정된 독해) |
|---|---|---|---|---|
| Team satisfaction | | | | |
| Way-of-working | | | | |
| Work-management | | | | |
| Comms candor | | | | |
| Mistake sharing | | | | |
| Motivation | | | | |
| Independence | | | | |
| Conflict converge | | | | |
| Change acceptance | | | | |
| Work satisfaction | | | | |

**Reconciliation checks (대조 체크):**
- Two metrics that should correlate but show a *negative* correlation → either one score is
  unreliable, or a hidden third cause (often management dissatisfaction). (상관 높아야 할 두
  지표가 음의 상관 → 신뢰도 낮은 점수 또는 숨은 제3원인(흔히 매니지먼트 불만).)
- High satisfaction with people but falling satisfaction with *way of working* → coach both the
  management layer and self-management at the individual level. (사람 만족 높고 *일하는 방식*
  만족 하락 → 매니지먼트와 개인 self-management 양쪽 코칭.)
