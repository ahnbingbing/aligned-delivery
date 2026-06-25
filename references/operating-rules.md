# Operating rules of thumb (운영 경험칙)

Heuristics distilled from **26 months of real product-team data**, generalized (no company
or project names, no proprietary figures beyond ratios). These are the footprint (도) —
empirical traces — so treat them as strong priors, not laws: they tell you where to look and
what "healthy" tends to mean, but always reconcile them against the team's live operating
state (기) before acting.

> **KO.** **26개월간의 실제 프로덕트 팀 데이터**에서 정제한 경험칙을 일반화한 것이다(회사·
> 프로젝트명 없음, 비율 외 독점 수치 없음). 이들은 흔적(도) — 경험적 발자취 — 이므로 법칙이
> 아니라 강한 사전확률(prior)로 다루어라: 어디를 보고 무엇이 "건강한" 상태인지를 알려주지만,
> 행동 전에 반드시 팀의 살아있는 운영 상태(기)와 대조하라.

Read this before interpreting any metric or script output, so your thresholds match the
method. (지표나 스크립트 출력을 해석하기 전에 읽어라 — 임계값이 방법론과 일치하도록.)

## Contents (목차)

**Core nine — the footprint (도) picture (#1–9):**
1. Predictability is the leading indicator of sustainable productivity
2. Ticket fragmentation index = completed tickets / completed SP
3. Operations ratio > ~50% collapses cross-role correlation (+ per-capita imbalance)
4. Workload volatility (STDEV) is a debt
5. Brooks' law holds when predictability is broken
6. Health-check "correction"
7. Confidence-level (self-assessment) tracked over time
8. When tooling changes throughput, measure output per cost — not just velocity
9. When the estimation unit breaks, move from tickets to the working product
- Using the rules together (규칙을 함께 쓰기)

**Footprint (도) — extended heuristics (#10–16):**
10. Pipeline time-lag: upstream load leads downstream output by ~1–2 sprints
11. Sustained core-role overload predicts next month's ops/incident spike
12. Mid-sprint scope expansion beyond ~30% collapses predictability
13. Backlog over-accumulation predicts next month's uncontrolled scope creep
14. A strategic cool-down is leading-indicator investment, not lost time
15. QA/SR throughput is a leading indicator of delivery completion
16. On onboarding/merge, correlation recovers before per-head SP — read correlation

**Operating-state (기) signals (#17–20):**
17. Psychological safety is the leading 기 metric; co-drop + widening STDEV = polarization
18. Read health by role — leadership can be RED while makers are GREEN
19. "Team management capability" is the canary metric
20. A leadership departure ripples through psychological safety

**Cross-layer (기 → 도) — directional hypotheses (#21–23):**
21. Psychological-safety decline (기) precedes quality & predictability problems (도)
22. Pushed velocity / scope volatility (도) degrades 기 — leadership first
23. A green footprint over a heavy corrected health-check = dig, not relax

**Decision / estimation / sequencing layer (#24–29):**
24. Decision-making — honesty is a DMF, not an ethics code
25. Estimation discipline: precision before accuracy
26. Set actionable metrics, not vanity ones
27. Read delivery health as speed AND stability — the DORA four keys
28. Sequence by economic priority — Cost of Delay / WSJF
29. Each cycle, name your scope mode

---

## 1. Predictability is the leading indicator of sustainable productivity (예측도가 지속가능한 생산성의 선행지표)

Protect **scope predictability ≥ ~90%**. High output on broken predictability is "fake
productivity" / debt — it gets repaid later. Predictability leads; velocity and on-time
delivery lag. When you must choose, stabilize predictability first and let velocity follow.

> **KO.** **스코프 예측도 ≥ ~90%** 를 지켜라. 예측도가 깨진 채 나오는 높은 산출은 "가짜
> 생산성"이자 부채이며, 나중에 갚게 된다. 예측도는 선행하고 벨로시티·정시 출시는 후행한다.
> 선택해야 한다면 예측도를 먼저 안정화하고 벨로시티가 따라오게 하라.

> *Calibration:* in an observed agile transition, over-commit (scope estimate ~111%) corrected toward
> ~100% as the team matured — supporting "calibrated ~100%" as the healthy target. (캘리브레이션:
> 관측된 애자일 전이에서 과커밋(스코프 추정 ~111%)이 성숙과 함께 ~100%로 보정됨 — "calibrated ~100%"
> 목표를 지지.)

→ Surfaced by `scripts/sprint_predictability.py` (scope% / completion% / RAG).

## 2. Ticket fragmentation index = completed tickets / completed SP (티켓 파편화 지수)

Above **~2.0**, context-switching costs cut effective output by roughly a sixth. Split work
toward **~0.5 SP** per item for visibility — **but avoid over-fragmentation**, which is its
own tax. The index is a band to stay inside, not a number to maximize.

> **KO.** **~2.0** 을 넘으면 컨텍스트 스위칭 비용이 유효 산출을 약 1/6 깎는다. 가시성을 위해
> 업무를 항목당 **~0.5 SP** 쪽으로 쪼개되, **과파편은 피하라** — 과파편 자체가 또 다른 세금이다.
> 지수는 최대화할 숫자가 아니라 머물러야 할 밴드다.

Estimates are only trustworthy for small items: prediction-vs-actual correlation is strong up to
~1 SP and weak beyond it, so **split anything larger than ~1 SP** to keep planning predictable.
(추정 신뢰는 작은 항목에서만 — 예측↔실측 상관이 ~1SP까지 강하고 그 이상은 약하다. **~1SP 초과는
쪼개라** 예측 가능성을 위해.)

→ Surfaced by `scripts/workload_fragmentation.py`.

> **Calibration (12-mo product-team data).** Real avg ≈ **0.57 SP/ticket** (so frag
> ≈ 1.75 on estimated tickets) — the ~0.5 SP target holds. But the index is
> **sensitive to unestimated (blank-SP) tickets**: counting them pushed the same
> team from 1.75 to **2.09** (just over the line). Read the 2.0 line together with
> estimation coverage, not as an absolute. (실데이터: 티켓당 ~0.57 SP. 무추정 티켓을
> 세느냐에 따라 1.75↔2.09로 갈리므로, 2.0 선은 추정 커버리지와 함께 읽어라.)

## 3. Operations ratio > ~50% collapses cross-role correlation (운영 비중 >50%는 교차 역할 상관을 무너뜨린다)

When operations work exceeds **~50%**, the pipeline fragments into "each-for-themselves"
(각자도생) and roles stop moving together. Keep ops in a **~25–35%** band. A low or negative
cross-role correlation (< ~0.1) is a silo-risk signal even before morale drops.

> **KO.** 운영 업무가 **~50%** 를 넘으면 파이프라인이 "각자도생"으로 파편화되고 역할들이
> 함께 움직이지 않는다. 운영을 **~25–35%** 밴드로 유지하라. 낮거나 음수인 교차 역할 상관
> (< ~0.1)은 사기가 떨어지기 전부터 사일로 위험 신호다.

**And read correlation as more than a silo alarm — it is the single biggest determinant of
output.** In 26 months of data, cross-role correlation vs team velocity regressed at **R²≈0.78** —
synchronization rate is the strongest mathematical variable setting total output volume. So
raising sync (not headcount) is often the highest-leverage move. (그리고 상관을 사일로 경보 이상으로
읽어라 — 산출량의 단일 최대 결정변수다. 26개월 데이터에서 교차역할 상관↔팀 velocity 회귀는
**R²≈0.78** — 동기화율이 총 산출 볼륨을 정하는 가장 강한 변수다. 인원이 아니라 싱크를 올리는 게
대개 최고 레버리지.)

→ Surfaced by `scripts/workload_fragmentation.py` (ops ratio + cross-role correlation).

> **Calibration (12-mo data).** Clan ops ≈ **31%** sat squarely in the 25–35% band
> and a human analyst independently called it "healthy" — band confirmed. The
> weakest role pair surfaced as **BE↔Design (≈ −0.2)**, the same silo a human
> review flagged (design→server reflected with a lag). Low/negative correlation
> is a real, early silo read. (실데이터: 전체 운영 ~31%로 25–35% 밴드 적중·"건강"
> 판정 일치; 최약 페어 BE↔Design ≈ −0.2 = 사람 리뷰가 짚은 사일로와 동일.)

### Workload imbalance is PER-CAPITA, not raw total SP (부하 불균형은 인당 기준)

A role with more people naturally shows more *total* SP — that is team size, not
overload. Measure imbalance as the coefficient of variation across roles of
**per-capita** SP. **CV > ~0.5 => high imbalance.** Also watch the absolute
per-capita ceiling: with optimal ≈ **12 SP/person/month** and max-available ≈
**15.5**, a role above 15.5 is overloaded even if the team is *balanced*.

> **KO.** 인원이 많은 역할은 *총* SP가 당연히 크다 — 그건 규모지 과부하가 아니다. 불균형은
> 역할별 **인당** SP의 변동계수로 보라(**CV > ~0.5 = 높은 불균형**). 절대 천장도 함께:
> 적정 ≈ **인당 월 12 SP**, 최대 가용 ≈ **15.5** — 팀이 *균형*이어도 15.5를 넘는 역할은 과부하다.

> **Calibration (12-mo data).** On raw total SP the CV read **0.60 ("imbalanced")**,
> but **per-capita CV was 0.15 ("balanced")** — matching the human analyst's
> "evenly distributed". The real story was **overload, not imbalance**: a balanced
> team with BE/FE per-capita (16–19) over the 15.5 ceiling. Pass `headcount` to
> `workload_fragmentation.py` for the per-capita read. (실데이터: 원시 SP CV 0.60
> "불균형"이지만 인당 CV 0.15 "균형" — 진짜 문제는 불균형이 아니라 BE/FE가 15.5 천장을
> 넘은 *과부하*. headcount 열을 주면 인당으로 읽는다.)

## 4. Workload volatility (STDEV) is a debt (업무량 변동성(표준편차)은 부채다)

A heroic, high-variance month is typically repaid over the next **1–3 months** in forced
cooldown, idle capacity, and operations. **Stability > heroics.** A steady 60%-pace
contributor usually out-delivers a high-variance "star" over a year; the star's output just
*looks* bigger in the impressive moments.

> **KO.** 영웅적이고 변동성 큰 한 달은 보통 이후 **1–3개월** 동안 강제 쿨다운, 유휴 캐파,
> 운영으로 갚게 된다. **안정성 > 영웅주의.** 꾸준한 60% 페이스의 기여자가 1년 단위로는
> 변동성 큰 "스타"보다 대개 더 많이 딜리버한다 — 스타의 산출은 인상적인 순간에 더 커
> *보일* 뿐이다.

**Automation/standardization mainly cuts volatility, not volume.** In the data, introducing
no-code automation raised average workload ~12% yet cut its STDEV **~57%** (4.2→1.8). Since the
volatility *is* the debt, automate routine work to stabilize the swing, not to shrink the total.
(자동화·표준화는 업무량이 아니라 *변동성*을 줄인다 — 노코드 자동화 도입 후 평균 업무량은 ~12%
늘었지만 STDEV는 **~57%** 줄었다(4.2→1.8). 변동성이 곧 부채이니, 총량을 줄이려고가 아니라 널뛰기를
잡으려고 루틴 업무를 자동화하라.)

> *Calibration:* in the agile transition, per-part daily-SP variance roughly halved (0.24→0.12) as
> the team matured — supporting volatility-reduction as a maturity signal. (캘리브레이션: 애자일
> 전이에서 직군별 일SP 분산이 성숙과 함께 약 절반(0.24→0.12)으로 — 변동성 감소가 성숙 신호임을 지지.)

→ Surfaced by `scripts/sprint_predictability.py` (workload STDEV).

## 5. Brooks' law holds when predictability is broken (예측도가 깨지면 브룩스 법칙이 작동한다)

Adding people to a late, low-predictability effort raises context-switching cost more than
it adds throughput. Whether Brooks' law bites depends on **team-building maturity** and the
**agility level** of both the team and the new hire: if both are low it bites hard; if both
are high (and the new hire is agile) it may not. The single biggest mitigator is **prior
shared history with *this* team**: borrowing a senior who has already worked with the team
mostly does *not* bite (the context-switching cost is already paid), whereas dropping in a
senior with no history into a mid-project, heavy-context domain genuinely doesn't help. But a
late schedule usually signals a **scope** problem, not only a headcount one — fix scope first
(PERT, scope hammering) before adding people.

> **KO.** 늦고 예측도 낮은 작업에 사람을 더하면 처리량보다 컨텍스트 스위칭 비용이 더 늘어난다.
> 브룩스 법칙이 무는지는 **팀빌딩 성숙도**와 팀·신규 인력 양쪽의 **애자일리티 레벨**에 달려
> 있다 — 둘 다 낮으면 강하게 물고, 둘 다 높고 신규 인력도 민첩하면 안 물 수도 있다. 가장 큰
> 완화 요인은 **이 팀과의 사전 협업 이력**이다: 이미 함께 일한 적 있는 시니어를 잠시 빌리는 건
> 대개 물지 않지만(컨텍스트 비용을 이미 치름), 이력 없는 시니어를 프로젝트 한복판·무거운
> 도메인에 꽂는 건 정말 도움이 안 된다. 다만 일정 지연은 보통 인력 문제만이 아니라 **스코프**
> 문제 신호다 — 사람을 더하기 전에 스코프부터 (PERT, 스코프 해머링) 고쳐라.

## 6. Health-check "correction" (헬스체크 "보정")

Reconcile survey **scores** with the positive/negative **wording** collected in 1:1s to
recover the *true* state — **scores alone over-report.** Two metrics that should correlate
but show a *negative* correlation mean either (a) one score is unreliable, or (b) a hidden
third cause (often dissatisfaction with management). Run the survey to get the prompt; run
the 1:1 to get the verdict.

**The size *and direction* of the correction gap is itself the signal.** A high raw score with a
large *downward* correction = suppression / score-gaming (a "looks-great" report hiding real
discomfort — watch this person). A low raw score that corrects *upward* = a macro/organizational
bias dragging an otherwise-fine individual down (less worrying than it first looks). So read the
gap, not just the corrected number.

> **KO.** **보정 갭의 크기*와 방향*이 곧 신호다.** 높은 원점수 + 큰 *하향* 보정 = 억압/점수
> 어뷰징("좋아 보이는" 보고가 실제 불편을 가림 — 주시 대상). 낮은 원점수가 *상향* 보정 = 멀쩡한
> 개인을 끌어내린 거시·조직 차원의 bias(첫인상보다 덜 걱정스러움). 보정된 숫자만이 아니라 갭을
> 읽어라.

> **KO.** 설문 **점수**를 1:1에서 수집한 긍정/부정 **표현**과 대조해 *진짜* 상태를 복원하라 —
> **점수만으로는 과대보고된다.** 상관이 높아야 할 두 지표가 *음의* 상관을 보이면 (a) 한
> 점수의 신뢰도가 낮거나, (b) 숨은 제3원인(흔히 매니지먼트 불만)이 있다는 뜻이다. 설문으로
> 질문을 얻고, 1:1로 판정을 얻어라.

→ Worksheet produced by `scripts/health_check_analyze.py`.

## 7. Confidence-level (self-assessment) tracked over time (시간에 걸쳐 추적하는 컨피던스 레벨)

A [0,1] self-assessment of goal confidence, checked periodically, doubles as an
individual-care signal and a collaboration trigger in standups. Don't cross-verify it
bluntly — that stunts growth. Treat the first score as a **baseline**, project forward, and
at the next checkpoint discuss whether it was well-calibrated, refining the person's scoring
logic over many cycles. It teaches quantifying the qualitative, gives each person an
objective cohort signal for self-review, and gives the manager an early-warning and
grouping signal.

> **KO.** 목표 달성 자신감을 [0,1]로 주기적으로 자가평가하는 지표는 개인 케어 신호이자
> 스탠드업의 협업 트리거 역할을 겸한다. 무디게 교차검증하지 마라 — 성장을 막는다. 첫 점수를
> **베이스라인**으로 두고 앞으로 투영한 뒤, 다음 체크포인트에서 잘 보정되었는지 논의하며 여러
> 사이클에 걸쳐 채점 로직을 정교화하라. 이는 정성을 정량화하는 법을 가르치고, 개인에게
> 자기 회고용 객관 코호트 신호를 주며, 매니저에게는 조기 경보·그룹핑 신호를 준다.

**During upheaval, read confidence the other way too — as a hypothesis, not a verdict.** In a
merge, reorg, or crisis, a **sustained high** confidence level (e.g., a weekly average staying
≥ ~0.8 while the ground is visibly shifting) *may* be a *false-normal* signal — suppression or
over-reporting, the same failure mode as "nobody is raising any issues." But it may also be
genuine: a mature team absorbing a natural change can be honestly calm. So treat calm-amid-
turbulence as a prompt to check the true state via 1:1 wording, not as an automatic alarm. And
note the converse for the leader's own conduct: **proximity ≠ alarm.** Getting closer (more
1:1s) is right, but a PM visibly running an emergency itself spreads anxiety — read the wave
without broadcasting danger; model calm.

> **KO.** **격변기엔 컨피던스를 거꾸로도 읽어라 — 단, 판정이 아니라 가설로.** 병합·조직개편·위기
> 중 컨피던스가 **지속적으로 높으면**(예: 바닥이 흔들리는데 주간 평균 ≥ ~0.8) 그건 *거짓 이상
> 상태(false-normal)* — 억압·과대보고("아무도 이슈를 안 꺼낸다"와 같은 실패 모드) — 일 *수*
> 있다. 하지만 진짜일 수도 있다: 성숙한 팀이 자연스러운 변화를 흡수할 땐 정말로 차분할 수 있다.
> 그러니 난기류 속 잠잠함은 자동 경보가 아니라 1:1 표현으로 진짜 상태를 *확인할 신호*로 다뤄라.
> 그리고 리더 자신의 처신엔 역도 성립한다 — **근접성 ≠ 경보.** 가까이 가는 것(1:1 늘리기)은
> 옳지만, PM이 눈에 띄게 비상을 돌리는 것 자체가 불안을 퍼뜨린다. 위험을 방송하지 말고 파동을
> 읽되 차분함을 모델링하라.

**Roll it out in sequence, or it breeds doubt.** Teams distrust a weekly confidence level when
the *action* is enforced before the skill and the meaning land. The order matters: (1) first let
the team acquire the skill of expressing the qualitative quantitatively — get comfortable putting
a feeling on a [0,1] scale; (2) once that's embodied, have them reason out the "why" *themselves*
— this is what raises their self-management level; (3) *only then* explain the "why" (a self-review
time-series + a care system) to confirm and deepen it. Don't hand them the meaning before they've
reached for it (무위) — explaining first stunts the self-management you're trying to grow.

> **KO.** **순서대로 굴려라 — 안 그러면 의구심을 낳는다.** 팀은 기술과 의미가 자리 잡기 전에
> *액션*이 강요되면 주간 컨피던스를 불신한다. 순서가 중요하다: (1) 먼저 정성적인 것을 정량적으로
> 표현하는 법을 체득하게 하라 — 느낌을 [0,1]로 옮기는 데 익숙해지기; (2) 체득되면 "왜"를 *스스로*
> 생각하게 하라 — 이것이 셀프 매니지먼트 레벨을 올린다; (3) *그 다음에야* "왜"를 설명하라(자기
> 시계열 회고 + 케어 시스템)며 확인·심화시켜라. 스스로 닿기 전에 의미를 건네지 마라(무위) — 먼저
> 설명해버리면 키우려던 셀프 매니지먼트를 오히려 막는다.

## 8. When tooling changes throughput, measure output per cost — not just velocity (도구가 처리량을 바꾸면, 벨로시티가 아니라 비용당 산출을 보라)

A step-change in tooling (e.g., an AI coding assistant) can lift raw velocity without lifting
*efficiency*, because it moves cost from labor to spend (tokens / API budget / licenses). Add
the cost denominator: track **output per unit cost**, not output alone. A +40% velocity jump
that comes with a larger-than-40% rise in token/API spend is not a clean efficiency gain. Fold
AI/tooling spend into the productivity picture before you call a tooling change a win — and once
a steady capacity is found, this denominator (with overtime) is what you manage to hold ~80%.

> **KO.** 도구의 계단식 변화(예: AI 코딩 어시스턴트)는 *효율*을 올리지 않고도 raw 벨로시티를
> 올릴 수 있다 — 비용을 인건에서 지출(토큰/API 버짓/라이선스)로 옮기기 때문이다. 분모를 붙여라:
> 산출 자체가 아니라 **비용당 산출**을 추적하라. 토큰/API 지출이 40%보다 더 늘면서 나온 +40%
> 벨로시티는 깨끗한 효율 개선이 아니다. 도구 변화를 성과로 부르기 전에 AI·도구 지출을 생산성
> 그림에 포함하라 — 그리고 안정 캐파를 찾은 뒤에는 이 분모(+야근)가 ~80%를 유지하며 관리할 대상이다.

## 9. When the estimation unit breaks, move from tickets to the working product (추정 단위가 깨지면, 티켓에서 워킹 프로덕트로 옮겨라)

The long-run convergence "1 ticket ≈ 1 SP ≈ 1 MD" (coaching Q15) is what lets ticket counts
proxy productivity. A step-change (AI assistants, a major process shift) breaks it — the same
1 SP is no longer the old 1 SP — and the ticket system starts *hiding* productivity rather than
showing it. **Don't normalize the before/after away; the discontinuity itself is valuable data**
(it measures the tool's real effect). Declare the change a **baseline reset**, and shift the
measurement substrate toward the working product: auto-log dev-start / dev-complete (the log
need not live in Jira), build a lead-time dashboard from it, and re-establish the SP baseline by
cohort over the next recalibration cycle — not every sprint (changing estimation logic too often
destroys precision; coaching Q29).

**This is also the read for teams that *never* use story points.** SP and due dates are not
universal; the footprint (도) that every issue tracker emits regardless is **timestamps and
counts** — so lead time (created→resolved), cycle time (started→resolved), throughput, and flow
efficiency (cycle/lead) are the SP-free substrate. **Low flow efficiency means the work sits in
queues, not that people are slow** — it's a structure (리) / cooperation-layer (공조) read, so the
move is to unblock the pipeline, not to push velocity. (SP·마감일이 없어도 — 모든 트래커가 남기는
타임스탬프·카운트가 흔적이다: 리드/사이클타임·처리량·플로우 효율이 SP-free 토대. 낮은 플로우 효율은
사람이 느린 게 아니라 일이 큐에 쌓인 것 = 리/공조 신호 → 속도가 아니라 파이프라인을 풀어라.)

→ Surfaced by `scripts/flow_metrics.py` (throughput / lead time / cycle time / flow efficiency).

> **KO.** 장기 수렴 "1티켓 ≈ 1SP ≈ 1MD"(코칭 Q15)가 티켓 수로 생산성을 대리하게 해준다.
> 계단식 변화(AI 어시스턴트, 큰 프로세스 전환)는 이를 깨뜨린다 — 같은 1SP가 더는 옛 1SP가
> 아니다 — 그리고 티켓 시스템은 생산성을 보여주기보다 *가리기* 시작한다. **전후를 보정해 지우지
> 마라; 그 단절 자체가 도구의 실제 효과를 재는 귀중한 데이터다.** 변화를 **베이스라인 리셋**으로
> 선언하고, 측정 토대를 워킹 프로덕트로 옮겨라: dev-start/dev-complete를 자동 로깅하고(로그가
> 지라에 있을 필요는 없다) 거기서 lead time 대시보드를 만들며, SP 기준선은 매 스프린트가 아니라
> 다음 재보정 주기에 코호트로 다시 세워라(추정 로직을 너무 자주 바꾸면 precision이 무너진다; 코칭 Q29).

> **Caveat — merges differ from tooling step-changes.** This substrate-shift rule is for a
> *tooling/process* step-change. When the discontinuity is two teams **merging**, the priority
> is the opposite: converge on **one simple shared unit** (e.g., 1 MD ≈ 1 SP, a small bounded
> scale) so the two cohorts can read each other, rather than re-platforming measurement mid-merge.
> (단서 — 병합은 도구 계단식 변화와 다르다. 이 토대 전환 규칙은 *도구·프로세스* 계단식 변화용이다.
> 단절이 두 팀 **병합**일 때는 우선순위가 반대다 — 측정 토대를 갈아엎기보다 **하나의 단순한 공유
> 단위**(예: 1MD≈1SP, 작은 바운드 스케일)로 수렴해 두 코호트가 서로를 읽게 하라.)

> *Calibration:* in the agile transition, per-head daily SP drifted toward ~1.0 (SP≈MD) as
> estimation skill rose, while confidence rose too — empirical support for the 1 ticket ≈ 1 SP ≈ 1 MD
> convergence (coaching Q15). (캘리브레이션: 애자일 전이에서 추정 스킬↑에 따라 인당 일SP가 ~1.0
> (SP≈MD)으로 수렴하고 자신감도 동반 상승 — 1티켓≈1SP≈1MD 수렴(코칭 Q15)의 실증.)

---

## Using the rules together (규칙을 함께 쓰기)

These nine are one picture: **predictability** (1) is the headline leading indicator;
**fragmentation** (2), **ops ratio** (3), and **volatility** (4) are the three usual ways it
breaks; **Brooks' law** (5) is what *not* to do when it's already broken; the
**correction** (6) and **confidence-level** (7) are how you read the operating-state (기) layer
that the numbers can't show; and **cost-per-output** (8) and the **working-product substrate**
(9) keep the numbers honest when a tooling change moves the ground under them. Lead with the
leading indicator, then reconcile against people.

> **KO.** 이 아홉은 하나의 그림이다 — **예측도**(1)가 핵심 선행지표이고, **파편화**(2)·**운영
> 비중**(3)·**변동성**(4)이 그것이 깨지는 흔한 세 경로이며, **브룩스 법칙**(5)은 이미 깨졌을 때
> *하지 말아야 할* 것이다. **보정**(6)과 **컨피던스 레벨**(7)은 숫자가 못 보여주는 기(운영 상태)
> 층위를 읽는 방법이며, **비용당 산출**(8)과 **워킹 프로덕트 토대**(9)는 도구 변화가 바닥을
> 흔들 때 숫자를 정직하게 유지한다. 선행지표를 앞세우고, 사람과 대조하라.
>
> The rules below extend this: #10–23 with pipeline dynamics, operating-state (기) signals, and
> cross-layer (기→도) reads; **#24–29 add the decision/estimation/sequencing layer — honesty as a
> DMF (#24), precision-before-accuracy estimation discipline (#25), actionable-over-vanity metrics
> (#26), DORA speed+stability health (#27), economic prioritization / WSJF (#28), and per-cycle
> scope modes (#29).** Note: #27–29 are industry-standard frameworks integrated 2026-06-24, not
> distilled from the 26-month dataset.
> (아래 #10–23은 파이프라인 동역학·기 신호·교차층(기→도) 독해로, **#24–29는 의사결정·추정·우선순위
> 층 — 정직 DMF(#24)·정밀도 우선 추정 규율(#25)·행동지표(#26)·DORA 속도+안정성(#27)·경제적 우선순위
> WSJF(#28)·사이클별 스코프 모드(#29)로** 확장한다. #27–29는 26개월 데이터가 아니라 2026-06-24에
> 통합한 업계 표준 프레임워크다.)

---

## Footprint (도) — extended heuristics (#10–16)

> ⚠️ **Calibration caveat.** The thresholds below (≈30%, ≈20%, ≈+28pp, R/R² values) are priors
> from one 26-month context; use the *direction and band*, treat absolute numbers as
> re-verify-on-your-data. (아래 임계값은 한 26개월 맥락의 prior다 — *방향·밴드*로 쓰고 절대수치는
> 본인 데이터로 재검증하라.)
>
> ⚠️ **Correlation ≠ causation caveat.** Every R/R² below is a *correlation* — the lowest rung of
> evidence, not a cause. A correlation tells you where to look and what to watch as a leading
> indicator; it does NOT license "do X to get Y." Before acting on one as if it were causal, ask
> for the counterfactual (what would have happened without it?) and a mechanism, and prefer a
> small controlled change (one team, one cycle) over a team-wide intervention justified by R²
> alone. Read these as honest *signals* to investigate, the same discipline as rule #24. (아래 모든
> R/R²은 *상관* — 증거의 최하위 단계지 인과가 아니다. 상관은 어디를 볼지·무엇을 선행지표로 감시할지를
> 알려줄 뿐 "Y를 얻으려면 X하라"를 허가하지 않는다. 인과처럼 행동하기 전 반사실[그게 없었다면?]과
> 메커니즘을 물어라; R²만 믿고 전사 개입하기보다 한 팀·한 사이클 소규모 통제 변경을 택하라. 코칭 Q28.)

## 10. Pipeline time-lag: upstream load leads downstream output by ~1–2 sprints (파이프라인 시차 — 상류 부하가 1~2스프린트 뒤 하류 산출을 결정)

The PM→Design→BE→FE pipeline ripples with a lag. A T-month upstream-role load predicts the
downstream role's output ~1 month later (e.g., BE load at T vs FE load at T+1 regressed at
**R≈0.72**); a Design workload surge is the most precise *leading* indicator that the dev engine
is about to fire; requirements take ~1–2 months to mature into dev output. So read the upstream
role's load/idle as a leading indicator of the downstream role's near future — a BE bottleneck
today is forced FE idle in ~1–2 sprints.

> **KO.** PM→Design→BE→FE 파이프라인은 시차를 두고 파도친다. T월 상류 직군 부하가 ~1달 뒤 하류
> 산출을 예고한다(BE_T vs FE_T+1 **R≈0.72**); Design 부하 급증은 개발 엔진 점화의 가장 정밀한
> *선행* 지표이고, 요구사항은 ~1~2달 숙성 후 개발 산출로 터진다. 상류 직군의 부하/유휴를 하류의
> 가까운 미래 선행지표로 읽어라 — 오늘 BE 병목은 ~1~2스프린트 뒤 FE 강제 유휴다.

## 11. Sustained core-role overload predicts next month's ops/incident spike (코어 직군 과부하는 익월 운영/장애 폭증의 예고편)

When the core pipeline role (often BE) runs above its workload line for a stretch, the *following*
month's operations/incident-ticket share spikes (in the data, past it crossed ~40% or ~2× the
prior level; R²≈0.68). Overload now is deferred quality/ops debt — watch the core role's load as a
leading indicator of next month's ops burden, and protect it before the spike.

> **KO.** 코어 파이프라인 직군(흔히 BE)이 한동안 권장 부하선 위로 달리면, *다음* 달 운영/장애 티켓
> 비중이 폭증한다(데이터상 ~40% 또는 직전 대비 ~2배 돌파; R²≈0.68). 지금의 과부하는 이연된 품질·운영
> 부채다 — 코어 직군 부하를 익월 운영 부담의 선행지표로 보고, 폭증 전에 보호하라.

## 12. Mid-sprint scope expansion beyond ~30% collapses predictability (스프린트 중 스코프 팽창 ~30% 초과 시 예측도 붕괴)

It's not how the sprint *starts* but the mid-sprint re-scoping that decides it — descoping
discipline determines sprint success ~92% of the time. Once Initial→Final committed expansion
passes **~30%**, completion predictability falls *exponentially* (R²≈0.71): cognitive energy
fragments and even the originally-promised work slips. Cap mid-sprint growth; when new high-priority
work lands, the PM re-prioritizes and descopes rather than just piling on.

> **KO.** 스프린트는 *어떻게 시작하느냐*가 아니라 중간 재조정이 결정한다 — descoping 규율이 성공을
> ~92% 좌우한다. Initial→Final 커밋 팽창률이 **~30%** 를 넘는 순간 종료 예측도는 *기하급수적으로*
> 하락(R²≈0.71)한다: 인지 에너지가 분산되고 원래 약속한 업무조차 밀린다. 중간 팽창을 캡하라 — 계획외
> 고우선 업무가 들어오면 쌓지만 말고 PM이 우선순위를 재조정·descoping 하라.

## 13. Backlog over-accumulation predicts next month's uncontrolled scope creep (백로그 적체는 익월 통제불능 스코프크립의 선행 원인)

When unresolved backlog accumulates **~20%** above normal, the next month's unplanned mid-sprint
intake (scope creep) rises ~35% (R≈-0.68). An over-full backlog narrows the pipeline mouth so
unplanned work forces its way in mid-sprint. Drain backlog debt as a leading control, not after
the creep shows up.

> **KO.** 미해결 백로그가 평시 대비 **~20%** 이상 누적되면 다음 달 계획외 중간 유입(스코프크립)이
> ~35% 증가한다(R≈-0.68). 과적된 백로그는 파이프라인 입구를 좁혀 계획외 업무가 스프린트 도중
> 밀고 들어오게 한다. 크립이 나타난 뒤가 아니라 선행 통제로 백로그 부채를 빼라.

## 14. A strategic cool-down (with shape-up review) is leading-indicator investment, not lost time (전략적 멈춤(쿨다운)은 낭비가 아니라 선행 투자)

A deliberate pause lowers that month's velocity but raises the *next* sprint's scope predictability
~+28pp (R≈0.81), and a shape-up/review done during cool-down converges the next sprint's dev-output
error to within ~5% (R²≈0.69). The pause works only if you use it to untangle the pipeline (tech
debt, ambiguous requirements, next-work review) — not merely to rest.

> **KO.** 의도적 휴지기는 당월 벨로시티는 낮추지만 *직후* 스프린트의 스코프 예측도를 ~+28pp 올리고
> (R≈0.81), 쿨다운 중 shape-up/리뷰는 다음 스프린트 개발 산출 오차를 ~5% 이내로 수렴시킨다(R²≈0.69).
> 단, 그냥 쉬는 게 아니라 파이프라인의 엉킨 실타래(기술부채·모호한 요건·다음 업무 리뷰)를 푸는 데
> 써야 효과가 난다.

## 15. QA/SR throughput is a leading indicator of delivery completion (QA/SR 처리량은 종료율의 선행지표)

Quality and deploy-blocking tickets (SR/QA) gate the whole pipeline's exit. When their resolution
rate drops below ~70%, overall completion falls ~15pp even though feature dev finished — deploy
blocking (R≈0.78). Treat QA/SR turnover as a leading indicator of completion, not a side task.

> **KO.** 품질·배포블로킹 티켓(SR/QA)이 파이프라인 출구를 연다. 이들의 종료율이 ~70% 아래로
> 떨어지면 피처 개발이 끝났어도 배포 블로킹으로 전체 종료율이 ~15pp 하락한다(R≈0.78). QA/SR 회전을
> 부수 업무가 아니라 종료율의 선행지표로 다뤄라.

## 16. On onboarding/merge, correlation recovers before per-head SP — read correlation (온보딩/병합 땐 SP보다 상관이 먼저 회복 — 상관을 보라)

Right after new members join, per-head SP dips (~-12% over the first two sprints — onboarding tax /
Ringelmann), while cross-role correlation climbs first (e.g., 0.5→0.85). The rising correlation —
not the dipping SP — is the healthy signal that newcomers have aligned into the pipeline. Judge
integration by correlation recovery, not by short-term SP.

> **KO.** 신규 합류 직후 1인당 SP는 일시 하락(첫 2스프린트 ~-12% — 온보딩 텍스/링겔만)하지만, 교차역할
> 상관이 먼저 오른다(예: 0.5→0.85). 떨어지는 SP가 아니라 *오르는 상관*이 신규 인력이 파이프라인에
> 정렬됐다는 건강 신호다. 통합은 단기 SP가 아니라 상관 회복으로 판단하라.

---

## Operating-state (기) signals (#17–20)

## 17. Psychological safety is the leading 기 metric; co-drop + widening STDEV = polarization (심리적 안전감이 선행 기 지표 — 동반 하락 + STDEV 확대 = 양극화)

Candor and "safe to admit mistakes / not-knowing" are the leading operating-state metrics. When
they fall *together* into Amber **and** their STDEV widens, the team isn't just less happy — it is
*polarizing* (some resign themselves, some absorb the overload). Rising STDEV on a 기 metric =
hidden disagreement hardening into haves/have-nots, the precursor to silent attrition.

> **KO.** `진솔함`과 `실수/모름 공유`(심리적 안전감)가 선행 기 지표다. 둘이 *동반* 하락해 Amber에
> 들고 **동시에** STDEV가 확대되면, 팀은 단지 덜 행복한 게 아니라 *양극화*(일부 체념, 일부 과부하
> 흡수) 중이다. 기 지표의 STDEV 상승 = 숨은 이견이 부익부빈익빈으로 굳는 것, 조용한 이탈의 전조다.

## 18. Read health by role — leadership can be RED while makers are GREEN (직군별로 읽어라 — 메이커는 GREEN인데 리더십이 RED일 수 있다)

The team average hides role divergence. Maker roles can sit in GREEN with satisfaction tracking
output, while PM/leadership psychological-safety and change-acceptance crater — the load of
"responsibility without authority" concentrates on leadership first. Always disaggregate health by
role before concluding the team is fine.

> **KO.** 팀 평균은 직군 차이를 가린다. 메이커 직군은 만족도가 산출과 비례하며 GREEN에 있는데,
> PM/리더십의 심리적 안정감·변화수용도는 무너질 수 있다 — "권한 없는 책임"의 부하가 리더십에 먼저
> 쏠린다. 팀이 괜찮다고 결론 내리기 전에 항상 직군별로 분해해 읽어라.

## 19. "Team management capability" is the canary metric (`업무 관리 능력`이 카나리아 지표)

Of the health metrics, "team management capability" tends to be the lowest and the first/biggest to
drop — and its decline names a specific cause: forced speed + frequent priority changes + an
ownership/process vacuum (responsibility without authority). When it falls, the org is pushing
output (도) without the process/ownership that protects the team. It is the earliest 기 read that a
push is becoming damage.

> **KO.** 헬스체크 지표 중 `업무 관리 능력`이 대개 최하·최대 낙폭이고, 그 하락은 원인을 특정한다 —
> 무리한 속도전 + 잦은 우선순위 변경 + 오너십/프로세스 부재(권한 없는 책임). 떨어진다면 조직이 팀을
> 보호할 프로세스/오너십 없이 산출(도)을 밀어붙이는 중이다. 밀어붙임이 손상이 되어가는 가장 이른 기 신호.

## 20. A leadership departure ripples through psychological safety (리더 이탈은 심리적 안전감을 타고 번진다)

After a lead leaves, the shock shows as: distrust of "is leadership protecting or *surveilling* us?",
individuals quietly absorbing the defense of the team (burnout risk), and a dip in candor. It rarely
shows in averages — read it in 1:1s, and protect the people carrying the absorbed load. (Backs
coaching Q49.)

> **KO.** 리더가 떠난 뒤 충격은 이렇게 나타난다 — "리더십이 보호인가 *감시*인가" 불신, 일부 개인이
> 조용히 팀 붕괴를 방어(번아웃 위험), 진솔함 하락. 평균엔 거의 안 보인다 — 1:1로 읽고, 흡수 부하를
> 진 사람을 보호하라. (코칭 Q49 실증.)

---

## Cross-layer (기 → 도) — directional hypotheses (#21–23)

> ⚠️ These are *directional* reads strongly suggested by the qualitative data (half-yearly health +
> retro), not yet clean monthly lead/lag regressions. Promote to confirmed rules once 기↔도 are
> aligned on a monthly axis. (반기 cadence라 깔끔한 월간 회귀는 아직 없음 — 월간 정렬 자료가 생기면
> 입증 규칙으로 승격.)
>
> **First monthly-axis instance (12-mo Jira data, one part, one month).** A
> cooperation-state read held end-to-end: the weakest role pair was **Design↔BE
> (correlation ≈ 0.2, near-zero on the monthly SP series) — a cooperation-layer 기
> signal — and the same month its sprint scope predictability collapsed
> 89.8% → 57.6% (도)**, with the analyst attributing it to design→server reflected
> with a lag. One documented instance, not a regression — but the chain
> 기(공조 상관)→도(예측도) now has real-data support, not only qualitative.
> (실데이터 1사례: Design↔BE 상관 ~0.2(공조층 기 신호) → 같은 달 스프린트 범위 예측도
> 89.8→57.6%(도) 붕괴. 회귀는 아니지만 월간 축 첫 실증.)

## 21. (Headline) Psychological-safety decline (기) precedes quality & predictability problems (도) (심리적 안전감 하락(기)이 품질·예측도 문제(도)를 예고한다)

This is the skill's central thesis as a reading: when "safe to admit mistakes / not-knowing" drops,
people stop surfacing what they don't know → hidden risk accumulates → predictability and quality
degrade a cycle later. So a candor/safety decline is a *leading* indicator of a future 도 problem.
Belief is the load-bearing layer under performance — watch the 기 signal before the 도 number moves.

> **KO.** 이것이 스킬 중심 명제의 독해 버전이다 — `실수/모름 공유`가 떨어지면 사람들이 모르는 걸 안
> 꺼내고 → 숨은 리스크가 적체되고 → 한 사이클 뒤 예측도·품질이 저하된다. 즉 진솔함·안전감 하락은 미래
> 도 문제의 *선행* 지표다. 신념이 성과 아래 하중층이다 — 도 숫자가 움직이기 전에 기 신호를 보라.

## 22. Pushed velocity / scope volatility (도) degrades 기 — leadership first (밀어붙인 속도·스코프 변동(도)은 기를 무너뜨린다 — 리더십이 먼저)

The reverse coupling: a sustained output push (forced speed + frequent priority churn) without
process/ownership protection drags down management-capability and psychological-safety metrics — and
PM/leadership 기 collapses first, output 도 a cycle later. A prolonged 도-push is itself a leading
indicator of a coming 기 collapse.

> **KO.** 역방향 결합: 프로세스/오너십 보호 없는 지속적 산출 밀어붙임(속도전 + 잦은 우선순위 변경)은
> 업무관리능력·심리안전감 지표를 끌어내린다 — PM/리더십 기가 먼저 무너지고, 산출 도는 한 사이클 뒤다.
> 장기 도-밀어붙임은 그 자체로 다가올 기 붕괴의 선행지표다.

## 23. A green footprint over a heavy corrected health-check = dig, not relax (보정 후 무거워진 헬스체크 위의 초록 도 = 안심 말고 파고들기)

A concrete instance of "trust the disagreement": in the data, corrected health scores broadly fell
(▼0.3–0.6) in the very period annual productivity and predictability hit highs — green 도 sitting on
a softening 기. Don't average them away; that gap is the signal to dig.

> **KO.** "어긋남을 신뢰하라"의 구체 사례: 데이터에서 보정 헬스 점수가 전반 하락(▼0.3~0.6)한 바로
> 그 기간에 연간 생산성·예측도는 최고치였다 — softening 기 위의 green 도. 평균 내어 지우지 마라; 그
> 갭이 파고들 신호다.

---

## Decision-making (의사결정) — honesty is a DMF, not an ethics code (#24)

**Treat "honesty is the best policy" as a Decision-Making Framework, not (only) an ethics code.**
You keep the signal honest because **accurate information flow is the load-bearing input to every
decision** — optimistic or face-saving data produces confidently wrong calls. This is the
operational home of the principle by the same name in `principles.md`; the rules above are largely
its disguise. (정직 = 윤리강령이 아니라 의사결정 프레임워크. 정확한 정보 흐름이 모든 결정의 하중
입력이라서 — principles.md 동명 원칙의 운영판이고, 위 경험칙들이 대개 그 변장이다.)

- **The honest-signal rules are the DMF input.** Protect *real* predictability over the comforting
  number (#1, fake productivity = debt), correct over-reporting scores with 1:1 wording (#6), trust
  layer disagreement instead of averaging it (#21–23), keep numbers honest through a tooling
  step-change (#8–#9), and set actionable over vanity metrics (coaching Q&A). Garbage-in honesty
  breaks every downstream decision. (정직 신호 규칙들이 곧 DMF 입력이다.)
- **Route by scope, don't frame everything.** Decide *who decides / who is consulted* (DACI), and
  how wide to share — forcing every situation into a framework is itself a risk. Leave it
  deliberately incomplete and get collective intelligence from fast, honest information flow.
  (DACI로 범위를 정하라; 모든 상황을 프레임에 넣지 마라 — 미완성으로 두고 빠른 정직한 흐름의
  집단지성을 얻어라.)
- **Timebox by stakes.** Sort fast decisions from serious ones by impact / reversibility / business
  power; a PM ceiling of **~2 days**, then escalate (over 2 days is usually above the PM's scope).
  In regulated/high-severity domains, reversibility alone can't make a call "fast" — weight by user
  impact. (이해관계로 타임박스: 빠른 결정 vs 신중한 결정; PM ~2일 상한 후 에스컬레이션; 규제·고위험
  은 되돌림 가능성만으로 빠르게 가지 말 것.)
- **Ground truth beats the decider's view (genchi genbutsu).** The fastest path to a good decision
  is a process that pulls the field's honest signal quickly and accurately — not a longer
  deliberation at the top. (현장의 정직한 신호가 의사결정자의 시각을 이긴다 — 겐치겐부츠.)
- **Decision-routing tools, used complementarily (not religiously).** Pair RACI/DACI (roles) with
  **Bezos Type 1 / Type 2** (reversibility: one-way doors slow, two-way doors fast) — **but the
  reversibility heuristic breaks in regulated / high-severity domains**: a reversible payment bug
  still sits under a regulator, so there weight by *user impact*, not reversibility. For root cause,
  run **5 Whys**, and pair a senior with a junior to debias the chain (the senior's prior can
  short-circuit it). (RACI/DACI[역할] + Type1/2[되돌림: 일방향 문은 신중·양방향 문은 빠르게] —
  단 규제·고위험에선 되돌림이 깨지니 *유저 임팩트*로 가중. 근인은 5 Whys, 시니어+주니어 페어로
  디바이어싱. Q46·Q31.)
- **A DMF is a maturity signal — and knowing when to turn it OFF is the top rung.** A team whose
  decision rules shift by mood is early-stage; a consistent, algorithmic DMF marks higher maturity;
  the most mature managers also frame *when not to apply the framework* (small teams < ~15, per
  Dunbar, where a heavy DMF is a bottleneck). Don't force every situation into the framework —
  leave it deliberately incomplete and let fast, honest information flow carry the rest. (DMF는
  성숙 신호이고 *언제 끌지* 아는 게 최상위 단계 — ~15인 미만은 무거운 DMF가 병목. Q39.)

*The move:* when a decision stalls, surface the real state honestly to the smallest right group
(DACI scope) and decide on the timebox — don't polish the model. (막히면 모델 다듬지 말고 진짜
상태를 적정 그룹에 정직하게 드러내고 타임박스 위에서 결정하라.) Grounds: coaching Q39, Q46.

## 25. Estimation discipline: precision before accuracy — "a predictable failure beats an unpredictable success" (추정 규율: 정확도보다 정밀도 — "예측 가능한 실패가 예측 불가능한 성공보다 낫다")

Two different things: **accuracy** = how close an estimate lands to the truth; **precision** = how
*consistently* the same logic reproduces a result. Most teams chase accuracy and neglect precision —
backwards. Low accuracy with **high precision is fixable** (a stable bias can be corrected with a
multiplier once you see the cohort history); high accuracy with low precision can't be steered. So
for a low-agility team, target only ~60% accuracy first and pour the effort into precision: everyone
estimating with the *same logic*, repeatedly. **A predictable failure beats an unpredictable
success** — knowing imperfectly beats not knowing. And to keep precision, **don't re-tune the
estimation logic too often** (~6-month cadence, even if that bends the Scrum guide); re-tuning every
sprint destroys the cohort comparability that makes prediction possible (ties to rule #9 baseline
resets, coaching Q15/Q29).

> **KO.** **정확도**(추정이 진실에 얼마나 가까운가)와 **정밀도**(같은 로직이 얼마나 *일관되게* 결과를
> 재현하는가)는 다르다. 대부분 정확도만 좇고 정밀도를 놓친다 — 거꾸로다. 낮은 정확도+**높은 정밀도는
> 교정 가능**(코호트 히스토리가 보이면 안정적 bias는 배수로 보정); 높은 정확도+낮은 정밀도는 조준 불가.
> 그러니 애자일리티 낮은 팀은 정확도 ~60%만 먼저 잡고 정밀도에 힘을 쏟아라 — 모두가 *같은 로직*으로
> 반복 추정. **예측 가능한 실패가 예측 불가능한 성공보다 낫다** — 불완전하게라도 아는 게 모르는 것보다
> 낫다. 정밀도 유지를 위해 **추정 로직을 너무 자주 바꾸지 마라**(~6개월 주기; 스크럼 가이드에 다소
> 어긋나도) — 매 스프린트 재조정은 예측을 가능케 하는 코호트 비교성을 무너뜨린다. (규칙 #9·코칭 Q15/Q29.)

Forecasting capstone: once precision holds, run probabilistic **Monte Carlo forecasting** over the
throughput / cycle-time history to turn "precision" into a dated probability ("85% chance done by
date X") — see `scripts/forecast_montecarlo.py`. (확률적 예측 = Monte Carlo, throughput 이력 위에서
정밀도를 날짜 확률로 바꾼다; `scripts/forecast_montecarlo.py`.)

## 26. Set actionable metrics, not vanity ones — and don't dress failure up as success (행동지표를 세워라, 허무지표 말고 — 실패를 성공으로 포장하지 마라)

Company-level KPIs are too coarse to tell you what an individual project actually changed, so a
project that reports only vanity numbers ("overall %", totals that always look good) wastes the
real prize: the **validated-learning** signal that tells you what to improve next. Set
**actionable** success metrics — ones tied to a specific behavior/hypothesis the team can act on —
alongside the headline KPI, so management, the team, and the company can all honestly recognize the
outcome. **A senior PM dressing a failure up as success via clever metric framing is metric
abuse** — it deceives the whole company, breeds resentment, and ultimately drags org-wide
productivity down. An honestly-named failure with accurate behavioral metrics keeps everyone moving
toward customer/product success; a vanity "win" stalls it. This is the metric-design face of the
honesty DMF (#24). (회사 KPI는 개별 프로젝트가 실제로 무엇을 바꿨는지 말해주기엔 너무 거칠다 —
허무지표["전체 %"·늘 좋아 보이는 총량]만 보고하면 다음에 무엇을 개선할지 알려주는 **유효학습** 신호를
날린다. 헤드라인 KPI와 함께 **행동지표**(팀이 행동 가능한 특정 가설·행동에 묶인 지표)를 세워라. 시니어
PM이 지표 프레이밍으로 실패를 성공으로 포장하는 건 **지표 어뷰징** — 전사를 기만하고 시기를 낳고 결국
전사 생산성을 끌어내린다. 정직하게 명명한 실패가 허무한 "승리"보다 낫다. #24 정직 DMF의 지표설계 버전.
코칭 Q14.)

---

## Speed-and-stability, prioritization, scope mode — industry frameworks (#27–29)

> These three are **industry-standard frameworks integrated 2026-06-24**, not distilled from the
> skill's 26-month dataset. Read them as well-validated defaults that sit alongside the empirical
> heuristics above, not as findings from the same data. (이 셋은 26개월 데이터가 아니라 2026-06-24에
> 통합한 업계 표준 프레임워크다 — 위 경험칙과 나란히 두는 검증된 기본값이지 같은 데이터의 발견이 아니다.)

## 27. Read delivery health as speed AND stability — the DORA four keys (속도와 안정성을 함께 — DORA 4지표)

The skill's flow metrics cover the SPEED half (lead time, cycle time, throughput). The other half is
STABILITY, and the industry-validated set is **DORA's four keys**: (speed) **deployment frequency** +
**lead time for changes**; (stability) **change failure rate** (% of deploys causing a failure /
incident) + **MTTR / time to restore**. A team that ships fast but with a high change-failure-rate or
a slow restore is not healthy — and either half can be gamed in isolation, so read them as a pair.
*The move:* track all four; if deployment frequency rises while change-failure-rate also rises, stop
scaling and stabilize first. Surfaced by `scripts/flow_metrics.py` (it now reads optional
`deploys` / `failures` / `restore_hours` columns). Provenance: DORA / Accelerate, not the 26-month data.

> **KO.** 스킬의 플로우 지표는 *속도* 절반(리드타임·사이클타임·처리량)만 다룬다. 나머지 절반은
> *안정성*이고, 업계 검증 세트가 **DORA 4지표**다 — (속도) **배포 빈도** + **변경 리드타임**; (안정성)
> **변경 실패율**(장애·인시던트를 부른 배포 비율) + **MTTR / 복구 시간**. 빠르게 내보내도 변경 실패율이
> 높거나 복구가 느린 팀은 건강하지 않다 — 어느 한쪽도 단독으로는 게이밍될 수 있으니 한 쌍으로 읽어라.
> *행동:* 넷을 다 추적하라; 배포 빈도가 오르는데 변경 실패율도 함께 오르면 스케일링을 멈추고 먼저
> 안정화하라. `scripts/flow_metrics.py`가 표면화한다(선택 열 `deploys`/`failures`/`restore_hours`를
> 이제 읽는다). 출처: DORA/Accelerate, 26개월 데이터 아님.

## 28. Sequence by economic priority — Cost of Delay / WSJF (무엇을 다음에 — 우선순위)

Rule #24 (honesty-as-DMF) governs *who / how* you decide; this governs *what's next*. Default lens:
**Cost of Delay (CoD)** and **WSJF = Cost of Delay ÷ job size** — sequence by economic urgency, not
the loudest voice or FIFO. Lighter alternatives, pick the smallest that fits: **RICE** (Reach ×
Impact × Confidence ÷ Effort), **Kano** (basic / performance / delight), **MoSCoW** (must / should /
could / won't). *The move:* when the backlog is contested, score the top candidates by WSJF (or RICE)
and sequence by it; re-score as Cost of Delay changes. Provenance: industry frameworks
(SAFe / Reinertsen, Intercom, Kano), not the 26-month data.

> **KO.** 규칙 #24(정직 DMF)는 *누가/어떻게* 결정하느냐를, 이 규칙은 *다음에 무엇*이냐를 다룬다. 기본
> 렌즈: **지연 비용(Cost of Delay)**과 **WSJF = 지연 비용 ÷ 작업 크기** — 가장 큰 목소리나 FIFO가
> 아니라 경제적 긴급도로 순서를 정하라. 더 가벼운 대안 중 맞는 가장 작은 걸 골라라: **RICE**(Reach ×
> Impact × Confidence ÷ Effort), **Kano**(기본/성능/감동), **MoSCoW**(must/should/could/won't).
> *행동:* 백로그가 다툼이 될 때 상위 후보를 WSJF(또는 RICE)로 점수 매겨 순서를 정하고, 지연 비용이
> 바뀌면 다시 점수 매겨라. 출처: 업계 프레임워크(SAFe/Reinertsen, Intercom, Kano), 26개월 데이터 아님.

## 29. Each cycle, name your scope mode (매 사이클 스코프 모드를 명명하라)

Don't drift on scope — make it an explicit per-cycle choice: **Expand / Selective-expand / Hold /
Reduce**, chosen from the leading signals already in this file (scope predictability #1,
backlog→creep #13, cool-down #14). *The move:* at planning, declare the mode and the signal that
justifies it ("Hold — predictability dipped below ~90% two sprints running"), so the team and
stakeholders share one frame. Provenance: adapted from the YC / GStack scope-mode practice,
integrated 2026-06-24.

> **KO.** 스코프를 표류시키지 마라 — 사이클마다 명시적 선택으로 만들어라: **Expand / Selective-expand /
> Hold / Reduce**, 이 파일에 이미 있는 선행 신호(스코프 예측도 #1, 백로그→크립 #13, 쿨다운 #14)에서
> 고른다. *행동:* 플래닝에서 모드와 그것을 정당화하는 신호를 선언하라("Hold — 예측도가 두 스프린트
> 연속 ~90% 아래로 떨어짐") — 팀과 이해관계자가 한 프레임을 공유하도록. 출처: YC/GStack 스코프 모드
> 관행을 각색, 2026-06-24 통합.
