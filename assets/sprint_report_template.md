# Sprint Report Template (스프린트 리포트 템플릿)

Reads the **도 (footprint)** layer — the measurable footprint. Issue it to all DACI stakeholders
on a weekly (or per-sprint) cadence. **Lead with the leading indicator** (scope predictability),
then the lagging numbers. Metrics are the trace, not the whole being — pair this with the health
check for the operating-state (기) read. (측정 가능한 흔적인 **도** 를 읽는다. DACI 전원에게
주간(또는 스프린트) 단위로 발행. **선행지표(스코프 예측도)를 앞세우고** 후행 숫자를 뒤에.
지표는 흔적일 뿐이니 운영 상태(기) 독해를 위해 헬스체크와 함께.)

→ Populate the numbers with `scripts/sprint_predictability.py` (CSV cols:
`sprint, planned_sp, added_sp, completed_sp`). (숫자는 `sprint_predictability.py`로 채운다.)

---

## Sprint [N] — [dates] (스프린트 [N] — [기간])

### 1. Headline / RAG (헤드라인 / RAG)

- **Overall flag (종합 신호):** 🟢 / 🟡 / 🔴
- **One-line state (한 줄 상태):** 

### 2. Leading indicators (선행지표)

| Indicator (지표) | This sprint (이번) | Trend (추세) | Flag |
|---|---|---|---|
| Scope predictability (스코프 예측도) = planned / (planned+added) | % | ↑/→/↓ | |
| Workload STDEV (업무량 표준편차) over recent sprints | SP | | |
| Confidence level (컨피던스 레벨) avg | 0–1 | | |

### 3. Lagging indicators (후행지표)

| Indicator (지표) | This sprint (이번) | Trend (추세) |
|---|---|---|
| Completion predictability (완료 예측도) = completed / planned | % | |
| Completed SP / Velocity (완료 SP / 벨로시티) | SP | |
| Project plan-vs-actual % (프로젝트 계획 대비 %) | % | |

### 4. Diagnosis — 리·기·도 read (진단)

- **도 (footprint):** what the numbers say. (숫자가 말하는 것.)
- **기 (operating state):** what the health check / standup wave says. (헬스체크·스탠드업 파동.)
- **리 (latent structure):** recurring pattern behind it. (그 뒤의 반복 패턴.)
- **Reconciliation (대조):** where the layers disagree = where to dig. (층위가 어긋나는 곳 = 팔 곳.)

> Reminder: a green completion number over a broken scope-predictability number is *fake
> productivity* — debt, not health. (완료 숫자가 초록이어도 스코프 예측도가 깨졌다면 *가짜
> 생산성* — 건강이 아니라 부채.)

### 5. Actions (액션) — one concrete, owned move per finding (발견별 구체·담당 액션 하나)

| Finding (발견) | Action (액션) | Owner (담당) | Leading indicator to watch (지켜볼 선행지표) |
|---|---|---|---|
| | | | |

### 6. Risks & escalations (리스크·에스컬레이션)

- 
