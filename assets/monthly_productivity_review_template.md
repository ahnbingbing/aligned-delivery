# Monthly Productivity Review Template (월간 생산성 리뷰 템플릿)

A monthly read across the whole product team (multiple parts/roles). Wider lens
than the weekly sprint report: throughput, per-capita workload, cross-role
cooperation, sprint predictability, and the operations load — one month, one
picture. **Lead with leading indicators**, keep it dry but specific, and land
every finding on one owned, measurable move. Metrics are the trace (도), not the
whole being — pair with the health check for the operating-state (기) read.
(팀 전체를 월 단위로 읽는다. 주간 스프린트 리포트보다 넓은 렌즈: 처리량·인당 부하·교차역할
공조·스프린트 예측도·운영 부하. **선행지표를 앞세우고**, 담백하되 구체적으로, 발견마다
담당·측정 가능한 한 수로 착지. 지표는 흔적(도)일 뿐 — 운영 상태(기)는 헬스체크와 함께.)

> **Confidentiality (기밀).** This is an internal artifact. Use neutral labels
> (Part A/B, roles PM/FE/BE/Design), never personal names, project codenames, or
> brand/feature names. (개인명·프로젝트 코드명·브랜드명 금지; 중립 라벨만.)

→ Populate with the skill scripts:
> `scripts/workload_fragmentation.py` (CSV: `role, period, sp, tickets, ops_sp,
> headcount`) → per-capita workload, imbalance, cross-role correlation, ops ratio.
> `scripts/sprint_predictability.py` (CSV: `sprint, planned_sp, added_sp,
> completed_sp`) → scope/completion predictability, RAG.
> `scripts/health_check_analyze.py` → the 기 (operating-state) read.

---

## [Month YYYY-MM] Productivity Review — [team] (생산성 리뷰)

Data period (분석 기간): [start–end] · Working days (근무일수): [n] ([±%] vs prev)

### 1. Overview & RAG (개요·RAG)

- **Team RAG (팀 종합):** 🟢 / 🟡 / 🔴 — [one dry line: what held, what moved].
- Per part (파트별):
  | Part (파트) | RAG | One-line state (한 줄 상태) |
  |---|---|---|
  | A | 🟢/🟡/🔴 | |
  | B | 🟢/🟡/🔴 | |

> Keep it honest and kind: name what the team got right before what to fix.
> (잘한 것을 먼저 짚고, 고칠 것을 뒤에.)

### 2. Throughput (처리량) — created vs resolved

| Metric (지표) | This month (이번) | Prev (전월) | Δ | R3M |
|---|---|---|---|---|
| Resolved tickets (해결 티켓) | | | | |
| Resolved SP (해결 SP) | | | | |
| Created tickets / SP (생성) | | | | |
| Avg SP per ticket (티켓당 SP) | | | | |

> Read SP per ticket against ~0.5–0.6 (the visibility band). Note estimation
> coverage: unestimated tickets inflate the fragmentation index, so report both.
> (티켓당 SP는 ~0.5–0.6 밴드로. 무추정 티켓은 파편화 지수를 부풀리니 추정 커버리지도 함께.)

### 3. Workload & cooperation (부하·공조) — the leading read

| Role (역할) | Per-capita SP (인당 SP) | Headcount | vs ceiling 15.5 | vs optimal ~12 |
|---|---|---|---|---|
| PM | | | | |
| Design | | | | |
| BE | | | | |
| FE | | | | |

- **Imbalance (불균형):** per-capita CV = [ ] — [balanced / high (>0.5)]. *Measure
  per-capita, not raw total SP — a bigger role shows more total SP without being
  overloaded.* (인당 기준으로. 원시 총 SP는 인원수에 오염된다.)
- **Overload (과부하):** roles above the 15.5 per-capita ceiling = [ ]. A *balanced*
  team can still be overloaded. (균형이어도 천장을 넘으면 과부하.)
- **Cross-role correlation (교차역할 상관 — 공조층 기 신호):** avg = [ ];
  weakest pair = [ ↔ ] at [r]. Below ~0.1 = silo risk; a near-zero/negative pair
  is an early silo read even before morale dips. (최약 페어가 사일로 조기 신호.)

> Cooperation correlation is not just a silo alarm — in 12+ months of data it was
> the single biggest determinant of total output (R²≈0.78 vs velocity). Raising
> sync is often higher-leverage than adding people. (공조 상관 = 산출 최대 결정변수;
> 인원 추가보다 싱크 올리기가 대개 더 큰 레버리지.)

### 4. Sprint predictability (스프린트 예측도) — per part

| Part | Scope predictability (스코프 예측도) | Completion (완료 예측도) | Velocity | RAG |
|---|---|---|---|---|
| A | % | % | SP | |
| B | % | % | SP | |

> Scope predictability is the leading indicator; velocity is lagging. High output
> on broken scope predictability is *fake productivity* — debt, not health. A
> conservative team that *trims* scope mid-sprint (scope% > 100%) is disciplined,
> not failing. (스코프 예측도가 선행, 속도는 후행. 예측도 깨진 높은 산출 = 가짜 생산성.
> 스코프를 *줄이는* 팀은 규율 있는 것.)

### 5. Operations load (운영 부하)

| Role (역할) | Ops ratio = ops_sp / sp (운영 비율) | Flag |
|---|---|---|
| PM | % | |
| Design | % | |
| BE | % | |
| FE | % | |
| **Overall** | **%** | |

> Healthy band ~25–35%. Above ~50% the pipeline fragments to each-for-themselves
> (각자도생) and cross-role correlation collapses. Below the band can mean ops is
> deferred (watch for a later spike). (건강 구간 ~25–35%; >50% 사일로, 밴드 미만은
> 운영 이연 신호.)

### 6. 리·기·도 reconciliation (대조) — where layers disagree = where to dig

- **도 (footprint / 측정된 흔적):** what the numbers say this month.
- **기 (operating state / 운영 상태):** what the health check + standups say.
- **리 (latent structure / 잠재 구조):** the recurring pattern behind both.
- **Disagreement (어긋남):** e.g. green output (도) over a softening health score
  (기) = do **not** average it away; that gap is the signal. (초록 산출 위 약해지는
  기 = 평균 내지 말 것 — 그 갭이 신호.)

### 7. Actions (액션) — one concrete, owned move per finding (발견별 담당 한 수)

| Finding (발견) | Action (액션) | Owner (담당) | Leading indicator to watch (지켜볼 선행지표) |
|---|---|---|---|
| | | | |

### Appendix — headcount by role × part (부록 — 직군×파트 인원)

| Part | PM | Design | BE | FE |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

> Headcount feeds the per-capita workload read (§3). Keep it current — per-capita
> is only as right as the denominator. (인원수는 §3 인당 계산의 분모 — 최신 유지.)
