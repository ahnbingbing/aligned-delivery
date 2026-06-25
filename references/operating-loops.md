# Operating loops & ceremony design (운영 루프 & 의식 설계)

This is the depth layer for **Capability B (diagnose)** and **Capability C (design
cadence / feedback loops)**. It turns the 응축→해산→창발→무위 cycle and 무위
(minimal-interference) leadership into concrete ceremonies, health checks, 1:1 corrections,
sprint analytics, and retrospectives. Read it whenever you are reading a team's operating
state or designing how it should run. (이 문서는 **역량 B(진단)** 와 **역량 C(케이던스·
피드백 루프 설계)** 의 심화층이다. 응축→해산→창발→무위 사이클과 무위 리더십을 구체적인
의식·헬스체크·1:1 보정·스프린트 분석·회고로 옮긴다.)

## Contents (목차)

1. The cycle as the real rhythm (사이클이 진짜 리듬이다)
2. The cadence ladder (케이던스 사다리)
3. The half-yearly diagnostic loop (반기 진단 루프)
   - 3a. Health check + 1:1 "correction" (헬스체크 + 1:1 보정) — reads 기
   - 3b. Sprint & workload analytics (스프린트·워크로드 분석) — reads 도
4. Retrospectives — KPT and the spiral (회고 — KPT와 나선)
5. Designing loops for a specific team (특정 팀을 위한 루프 설계)
6. Merging two teams (두 팀 병합)
7. Designing planning & retro from the team's process signals (팀의 프로세스 신호로 플래닝·회고 설계)
8. Introducing agile / a process transition (애자일·프로세스 전이 도입)
9. Managing up — the third axis (위로 관리하기 — 세 번째 축)
10. People — motivation, candor & conflict (사람 — 동기·솔직함·갈등)

---

## 1. The cycle as the real rhythm (사이클이 진짜 리듬이다)

Every loop — a sprint, a quarter, a single incident — runs the same four beats. Design
ceremonies *onto* the beats rather than copying a framework wholesale.

| Beat | What happens | Ceremony that carries it |
|---|---|---|
| **응축 Condense** | Focus and diagnose one problem | Planning, backlog refinement, problem definition |
| **해산 Dissolve** | Break fixed plans; rearrange | Grooming, re-estimation, mid-sprint pivot |
| **창발 Emerge** | Let a new pattern appear | Review, demo, spike outcomes |
| **무위 Wu-wei** | Stabilize coherence with minimal force | Retro (KPT), guardrails, confidence-level check |

> **KO.** 모든 루프 — 스프린트, 분기, 단일 인시던트 — 는 같은 네 박자를 돈다. 프레임워크를
> 통째로 베끼지 말고 박자 *위에* 의식을 설계하라. **응축**(하나의 문제를 초점화·진단:
> 플래닝, 백로그 리파인먼트), **해산**(고정된 계획을 깨고 재배치: 그루밍, 재추정, 중간 피봇),
> **창발**(새 패턴이 나타나게 둠: 리뷰, 데모, 스파이크 결과), **무위**(최소한의 힘으로 일관성
> 안정화: 회고(KPT), 가드레일, 컨피던스 레벨 체크).

**무위 leadership in practice:** reduce interference so the system self-aligns. Prefer
guardrails (WIP limits, RAG thresholds, definition-of-done) and information transparency
over micromanagement. Leave a deliberate, *small* gap of unfilled decisions for the team to
fill — guideline ~3–5% of decision agenda for senior teams, under ~10% generally — so
ownership grows. (실천: 간섭을 줄여 시스템이 스스로 정렬하게 하라. 마이크로매니징보다
가드레일(WIP 제한, RAG 임계, DoD)과 정보 투명성. 팀이 채우도록 의도적으로 *작은* 의사결정
공백을 남겨라 — 시니어 팀 기준 의사결정 아젠다의 ~3–5%, 일반적으로 ~10% 미만.) The aim is to work
toward a team **"managed without being managed"** — model self-management yourself and earn the
step-back through trust so control becomes progressively unnecessary (principles #4). (목표는
'관리하지 않아도 관리되는' 팀으로 나아가는 것 — 리더가 먼저 자기관리를 모범 보이고 신뢰로 물러설
권리를 얻어 통제가 점점 불필요해지게 하라. 원칙 #4.)

---

## 2. The cadence ladder (케이던스 사다리)

A practical default set of loops, by period. Scale up or down to the team's maturity and the
project's complexity — don't impose heavy cadence on a team under ~15 people (Dunbar) where
it becomes a bottleneck. (성숙도와 복잡도에 맞춰 가감하라 — ~15인 미만(던바) 팀에 무거운
케이던스를 강요하지 마라; 병목이 된다.)

- **Minute-level (분 단위)** — the individual's own continuous loop *while building*:
  self-correction in the flow of the work. No ceremony — it rests on each person's
  **self-management**, the root the whole ladder is built on (the finer this loop, the lighter
  every loop above it needs to be).
- **Daily (일 단위)** — 15-min stand-up; clear blockers before the team starts;
  confidence-level as a care + collaboration trigger.
- **Weekly user touchpoint (주간 사용자 접점)** — a standing **continuous-discovery**
  contact with real users (Teresa Torres): a small, regular interview or session that keeps
  *fresh customer signal* flowing into the discovery engine. Discovery is a **rhythm**, not a
  one-off kickoff. **Move: put a standing weekly user touchpoint on the cadence** so the team
  never designs from stale assumptions.
- **Weekly (주 단위)** — a weekly sync or **refinement meeting**; epic / project / assignee
  level; dependency adjustment; a progress report to all DACI stakeholders.
- **Bi-weekly or 3-weekly (격주~3주, = sprint length)** — **sprint retrospective / planning, or a
  release review**; team-level; alignment with the management team.
- **Monthly (월 단위)** — **productivity review + roadmap review/planning** (product ↔
  business/marketing sync); productivity metrics (individual / team / product / ops / sprint).
- **Quarterly (분기)** — **product review & goals** (product-level review/planning; goal/OKR setting).
- **Half-yearly (반기)** — **process review & team-stability review** (health check + 1:1
  correction). This is the big diagnostic loop the scripts support.
- **Yearly (연 단위)** — **annual productivity analysis + vision review & alignment** — read the
  year's productivity metrics (individual / team / product / sprint) AND re-align the team to the
  vision/north star.

> **KO.** 분 단위(스스로 개발하며 도는 개인의 연속 루프 — 의식 없음, 각자의 **자기관리** 위에
> 올라가며 사다리 전체의 뿌리다; 이 루프가 촘촘할수록 위의 모든 루프가 가벼워진다), 일 단위(15분
> 스탠드업, 블로커 해소, 케어+협업 신호로서의 컨피던스 레벨), **주간 사용자 접점**(실제 사용자와의
> 상시 **지속 디스커버리** 접점 — 테레사 토레스: 작고 규칙적인 인터뷰가 *신선한 고객 신호*를 디스커버리
> 엔진에 계속 흘려보낸다; 디스커버리는 일회성 킥오프가 아니라 **리듬**이다. 무브: 상시 주간 사용자
> 접점을 케이던스에 두어 팀이 낡은 가정으로 설계하지 않게 하라), 주 단위(위클리 싱크 혹은 **리파인먼트
> 미팅**, 에픽·프로젝트·담당자 단위, 디펜던시 조정, DACI 전원 보고), 격주~3주(=스프린트 길이; **스프린트
> 회고/플래닝 혹은 릴리즈 리뷰**, 팀 단위, 매니지먼트 정렬), 월 단위(**생산성 리뷰 + 로드맵
> 리뷰/플래닝**, 제품↔사업 싱크, 생산성 지표), 분기(**제품 리뷰 & 목표** — 제품 단위 리뷰/플래닝,
> 목표/OKR 수립), 반기(**프로세스 리뷰 & 팀 안정성 리뷰** — 헬스체크 + 1:1 보정, 스크립트가 지원하는
> 큰 진단 루프), 연 단위(**연간 생산성 분석 + 비전 리뷰 & 얼라인먼트** — 한 해 생산성 지표(개인/팀/
> 제품/스프린트)를 분석하고 팀을 비전/북극성에 다시 정렬).

For Kanban-leaning teams, the equivalent is the **7 cadences** (Strategy/Operations/Risk
Reviews, Service Delivery Review, Delivery Planning, Replenishment, Daily Stand-up) with
**Classes of Service** (Expedite / Fixed-date / Standard / Intangible). (칸반 성향 팀은
**7 케이던스** 와 **CoS**(Expedite/Fixed-date/Standard/Intangible)로 대응한다.)

---

## 3. The half-yearly diagnostic loop (반기 진단 루프)

This is the loop that ties the scripts together. Run it as: **health check → 1:1 correction
→ sprint/workload analytics → diagnosis → action plan.** (스크립트들을 엮는 루프:
**헬스체크 → 1:1 보정 → 스프린트/워크로드 분석 → 진단 → 액션 플랜.**)

### 3a. Health check + 1:1 "correction" (헬스체크 + 1:1 보정) — reads 기 (operating state)

1. Run the quantitative survey (≈10 metrics, 1–5 scale). Analyze with
   `scripts/health_check_analyze.py` → averages, STDEV, period-over-period deltas,
   Amber/Green flags, **and the correction worksheet**.
2. Hold 1:1s. Fill the worksheet's positive/negative wording columns. **Scores over-report;
   the 1:1 wording sets the corrected read.** Watch for metrics that dropped period-over-
   period even while still Green, and for high-STDEV metrics (hidden disagreement).
3. Reconcile: if two metrics that should correlate show a negative correlation, suspect an
   unreliable score or a hidden third cause (often management dissatisfaction).

> **KO.** (1) 정량 설문(약 10문항, 1–5)을 `health_check_analyze.py`로 분석 → 평균·표준편차·
> 기간 델타·플래그·**보정 워크시트**. (2) 1:1에서 긍정/부정 표현 칸을 채운다 — **점수는
> 과대보고되며, 1:1 표현이 보정된 독해를 정한다.** 초록이어도 하락한 지표, 높은 표준편차(숨은
> 이견)에 주의. (3) 상관이 높아야 할 두 지표가 음의 상관이면 신뢰도 낮은 점수나 숨은
> 제3원인(흔히 매니지먼트 불만)을 의심하라.

### 3b. Sprint & workload analytics (스프린트·워크로드 분석) — reads 도 (footprint)

- `scripts/sprint_predictability.py` → scope/completion predictability, workload STDEV, RAG.
  Lead with **scope predictability** (the leading indicator); a green completion number over
  a broken scope number is fake productivity.
- `scripts/workload_fragmentation.py` → fragmentation index, cross-role correlation, ops
  ratio, imbalance. Use it to find silos (low/negative cross-role correlation, ops > ~50%).

Then reconcile the footprint (도) against the operating state (기): green metrics over a heavy
health check is the signal to dig, not to relax. (그다음 흔적(도)을 운영 상태(기)와 대조하라 —
무거운 헬스체크 위의 초록 지표는 안심이 아니라 파고들 신호다.)

---

## 4. Retrospectives — KPT and the spiral (회고 — KPT와 나선)

Use **KPT (Keep / Problem / Try)** as the default retro structure. The point is not to list
items but to close the **spiral**: each retro must produce **Try** items that change the next
loop, and the next retro must check what last time's Tries did. A retro that doesn't change
the next loop is theater. (기본 회고 구조로 **KPT(Keep/Problem/Try)** 를 써라. 핵심은 항목
나열이 아니라 **나선**을 닫는 것 — 모든 회고는 다음 루프를 바꾸는 **Try** 를 내야 하고, 다음
회고는 지난 Try가 무엇을 바꿨는지 점검해야 한다. 다음 루프를 바꾸지 않는 회고는 연극이다.)

**Timing matters.** Team-level retros are best at release or once operational stability is
reached (memory is volatile — do it before it evaporates). Stakeholder/decision-maker retros
belong *after* impact measurement — agree the measurement date at project kickoff so the
retro lands with it (suggested ~1.5–2 months post-release). (타이밍이 중요하다. 팀 회고는
릴리즈 시점 혹은 운영 안정화 직후가 최적(기억은 휘발한다). 이해관계자·의사결정자 회고는
*성과 측정 이후* — 착수 시점에 측정일을 합의해 회고가 그에 맞게 떨어지도록(릴리즈 후 ~1.5–2개월
제안).)

**Blameless postmortem — the variant for an incident or breakdown.** When the loop being
reviewed is a *failure* (an outage, a missed launch, a process collapse), KPT is the wrong
shape. Run a **blameless postmortem** instead: assume **everyone acted reasonably given what
they knew at the time**, and investigate the *system* — build the **timeline**, surface the
**contributing conditions**, and ask **what made the error easy to make** — never *who* made
it. This is honesty-as-DMF in action: it pairs with "proximity ≠ alarm" — the goal is to get
closer to the truth of the system, not to raise an alarm over a person. A name-and-blame
review teaches the team to hide the next incident. **Move: after an incident, run a blameless
postmortem (timeline → contributing factors → systemic fixes), never name-and-blame.**
(Provenance: Google SRE.)

> **KO.** **블레임리스 포스트모템 — 인시던트·붕괴용 변종.** 리뷰 대상 루프가 *실패*(장애, 출시
> 실패, 프로세스 붕괴)일 땐 KPT가 맞는 그릇이 아니다. 대신 **블레임리스 포스트모템**을 돌려라:
> **그 순간 알던 정보 하에선 모두가 합리적으로 행동했다**고 전제하고, *사람*이 아니라 *시스템*을
> 조사하라 — **타임라인**을 세우고, **기여 조건**을 드러내고, **무엇이 그 실수를 쉽게 만들었나**를
> 물어라. 정직 = DMF의 실천이며 "근접성 ≠ 경보"와 짝을 이룬다 — 사람에게 경보를 울리는 게 아니라
> 시스템의 진실에 가까이 가는 것이 목표다. 이름을 짚어 탓하는 리뷰는 팀에게 다음 인시던트를 숨기는
> 법을 가르친다. **무브: 인시던트 후 블레임리스 포스트모템(타임라인 → 기여 요인 → 시스템 수정)을
> 돌려라, 결코 이름-탓하기가 아니라.** (출처: 구글 SRE.)

Use the asset `assets/retro_kpt_template.md` to run it. (회고 진행에는
`assets/retro_kpt_template.md` 자산을 사용하라.)

---

## 5. Designing loops for a specific team (특정 팀을 위한 루프 설계)

When asked to design or fix an operating model, work in this order — it keeps you from
copying a framework instead of fitting one: (운영 모델 설계·수정 요청 시 이 순서로 — 프레임워크
복붙 대신 적합화를 보장한다.)

1. **Read 리·기·도 first.** Latent structure (team/backlog shape), operating state (health
   check + 1:1), footprint (sprint analytics). Name where the pain actually lives.
2. **Pick the leading indicator to protect.** Usually scope predictability; sometimes ops
   ratio or cross-role correlation if the pain is silos.
3. **Set guardrails, not scripts of behavior.** WIP limits, RAG thresholds, definition-of-
   done, a transparency ground rule ("annoying is better than silence").
4. **Choose the minimal cadence that closes the spiral.** Enough loops to learn and correct,
   not so many that tracking load smothers the work.
5. **Design proximity in.** 1:1 rhythm, role-wall-breaking syncs, confidence-level as a
   care + collaboration signal. In friction, get closer.
6. **Leave the small gap.** ~3–5% (senior) of decisions unfilled for the team to own.

> **KO.** (1) **먼저 리·기·도를 읽어라** — 잠재 구조, 운영 상태(헬스체크+1:1), 흔적(스프린트
> 분석). 고통이 실제로 어디 사는지 명명하라. (2) **지킬 선행지표를 골라라** — 보통 스코프
> 예측도, 사일로가 문제면 운영 비중·교차 역할 상관. (3) **행동 대본이 아니라 가드레일을 세워라**
> — WIP 제한, RAG 임계, DoD, 투명성 그라운드룰("침묵보다 시끄러움이 낫다"). (4) **나선을
> 닫는 최소 케이던스를 골라라** — 배우고 보정하기에 충분하되, 추적 부하가 일을 질식시키지
> 않게. (5) **근접성을 설계에 넣어라** — 1:1 리듬, 역할 벽 허물기 싱크, 케어+협업 신호로서의
> 컨피던스 레벨. 마찰엔 가까이. (6) **작은 공백을 남겨라** — 시니어 기준 의사결정의 ~3–5%를
> 팀이 소유하도록.

---

## 6. Merging two teams (두 팀 병합)

A merge is a request to rearrange two different **리 (de-facto structures)** — different tools,
estimation units, cadences, cultures — into one. Treat it as B-then-C, and accept up front that
**velocity will drop first; that is normal, not failure.** A practical first-30-days loop:

- **Day 1 — diagnose from the data *yourself*, first.** Mine each team's history (e.g., ~2 years
  of tickets) and form **your own read of the problems and a strategy** *before* engaging people —
  you walk into the 1:1s with hypotheses, not a blank page. Get observer access to each team's
  ceremonies, and tell both teams to **keep their own way until a joint method is agreed** (the
  first ~2 weeks).
- **Days 2–4 — 1:1s, practitioners before leads.** Run a short pre-1:1 survey (5-scale on
  motivation/state), then 1:1s (≈50 min). Do **practitioners first, leads last**, so you can
  synthesize the practitioner picture before the lead discussion. Then **data-mine survey + 1:1
  wording for positive/negative terms** to recover the true state (scores over-report — rule #6).
  Build a stakeholder map *per team* across several axes (tenure, ability, communication). Compare
  not just the **means** but the two teams' **score distributions** — a distribution mismatch is
  the real merge problem to solve.
- **Days 5–10 — observe.** Sit in. Identify each team's cultural strengths worth cross-pollinating.
- **~Day 15 — a vision-alignment session.** Open with a physical icebreaker (it lowers people's
  guard), mix members into cross-origin sub-teams, and have them build a shared answer to a forward
  framing ("what will the CEO say about our team a year from now?") using words that must include
  the good parts of *both* cultures. Close with a shared meal.
- **Then a shared low-stakes project** (tech debt is a good candidate) run as a real sprint, so the
  *new* members co-design the way of working (propose a draft, let them agree it). Use
  **constraint-driven cooperation + go-and-see** (cross-team code review, reading each other's
  actual artifacts) as the trust mechanism — see principle 5. Start a 1-week sprint before ~Day 20.

**What to measure (leading first):** per-cohort scope predictability (≥~90% recovery, units *not*
mixed), cross-origin correlation (< ~0.1 = one roof, two teams), ops ratio (25–35%), per-cohort
workload STDEV, and a confidence-level baseline. **What NOT to touch:** the first ~2 weeks; the
shuffling of current work (keep existing assignments, mix origins only on *new* work); and don't
force-unify estimation logic *and* cadence at once (you won't be able to read which one caused a
drop). Converge on **one simple shared unit** (1 MD ≈ 1 SP) rather than re-platforming measurement
mid-merge (rule #9 caveat). **Failure signals:** never judge by velocity (it drops first) — instead
watch for high per-sprint velocity variance, a **sustained-high confidence level (false-normal)**,
growing per-role workload variance, or "no issues" calm that doesn't match the turbulence (rule #7).

> **KO.** 병합은 서로 다른 두 **리(de-facto 구조)** — 도구·추정 단위·케이던스·문화 — 를 하나로
> 재배열하라는 요청이다. B→C로 다루고, **velocity는 먼저 떨어진다 — 정상이지 실패가 아니다**를
> 전제로 깔아라. 실전 첫 30일 루프:
> - **Day 1 — 데이터로 *먼저, 스스로* 진단하라.** 각 팀의 이력(예: ~2년치 티켓)을 분석해 사람을
>   만나기 *전에* **문제점과 전략 방안을 스스로 세워라** — 가설을 들고 1:1에 들어가라, 백지가 아니라.
>   각 팀 의식에 옵저버로 참석하고, **합동 방식 합의 전까지(첫 ~2주)는 각자 방식을 유지**하라고 전한다.
> - **Day 2–4 — 1:1, 실무진 먼저 리드 나중.** 1:1 전 짧은 설문(동기·상태 5-scale) → 1:1(약 50분).
>   **실무진 먼저, 리드 마지막** — 실무진 그림을 정리해 리드 논의에 들어가기 위함. 이후 **설문+1:1
>   표현을 데이터마이닝**해 긍정/부정 단어로 진짜 상태 복원(점수는 과대보고 — 규칙 #6). 스테이크홀더
>   맵을 *팀별로* 여러 축(연차·ability·커뮤니케이션)으로 그린다. **평균만이 아니라 두 팀의 점수
>   분포(표준분포)** 를 비교하라 — 분포 차이가 풀어야 할 진짜 병합 문제다.
> - **Day 5–10 — 옵저빙.** 들어가 본다. 서로에게 좋은 영향을 줄 각 팀 고유 문화를 식별.
> - **~Day 15 — 비전 얼라인먼트 세션.** 몸을 쓰는 아이스브레이커로 연다(경계가 낮아진다). 출신
>   섞은 소팀으로 나누고, **양쪽 문화의 좋은 점이 반드시 들어간** 단어들로 미래 프레이밍("1년 뒤
>   CEO는 우리 팀을 어떻게 평가할까?")에 대한 공동 답을 만들게 한다. 회식으로 닫는다.
> - **이후 공유 저난도 프로젝트**(기술 부채가 좋은 후보)를 실제 스프린트로 돌려 *새* 팀원들이 일하는
>   방식을 공동 설계하게 한다(초안 제안 → 팀이 합의). 신뢰 메커니즘으로 **제약기반 협력 + 현지현물**
>   (교차 코드리뷰, 서로의 실제 산출물 읽기)을 써라 — 원칙 5 참고. ~Day 20 전에 1주 스프린트 시작.
>
> **측정(선행지표 먼저):** 코호트별 스코프 예측도(≥~90% 회복, 단위 *섞지 말 것*), 교차 출신 상관
> (< ~0.1 = 한 지붕 두 팀), 운영 비중(25–35%), 코호트별 업무량 STDEV, 컨피던스 베이스라인.
> **건드리지 않을 것:** 첫 ~2주; 현재 업무의 셔플링(기존 배정 유지, *새* 업무에만 출신 섞기); 추정
> 로직과 케이던스를 동시에 강제통일하지 말 것(드롭 원인을 못 읽는다). 측정을 갈아엎기보다 **하나의
> 단순 공유 단위**(1MD≈1SP)로 수렴(규칙 #9 단서). **실패 신호:** velocity로 판단하지 마라(먼저
> 떨어진다) — 대신 스프린트별 velocity 편차 큼, **컨피던스 지속 고점(거짓정상)**, 직군별 업무량
> 편차 증가, 난기류와 안 맞는 "이슈 없음" 잠잠함을 보라(규칙 #7).

---

## 7. Designing planning & retro from the team's process signals (팀의 프로세스 신호로 플래닝·회고 설계)

Retro data surfaces three design rules for *how* to run planning and retros:

- **Planning support has a middle zone — both extremes hurt.** Satisfaction with PM/TL planning
  support drops at *either* pole: too detailed (micromanaging) **and** too sparse (title-only
  tickets dumped without context, roadmap shared with only some, or priorities changed too often).
  The healthy zone: a clear sprint goal + priorities, shared with *everyone*, not over-churned. An
  unclear sprint goal is consistently the #1 planning blocker; unplanned high-priority intake and
  priority churn are the #1 execution blockers.
- **Build a structural buffer or you get chronic overpace.** With no planning buffer, work slips to
  the next sprint and the team lives in permanent overpace. Leave explicit buffer, and have the PM
  *drive* re-prioritization/descoping when new work lands (don't let it silently pile on).
- **Above ~10 people, split the scrum; make the retro close the spiral or it's theater.** Teams
  past ~10 should divide (echoes the <15 Dunbar cadence note); when people doubt "why a KPT every
  2 weeks?", the spiral isn't closing. Make celebrating each other's learning and *tracking last
  time's improvements* an explicit part of the process — and leaders must step out of micromanaging.

> **KO.** 회고 데이터가 플래닝·회고 *운영 방식*에 대한 세 가지 설계 규칙을 드러낸다:
> - **플래닝 지원은 중간 지대가 있다 — 양극단이 다 해롭다.** PM/TL 플래닝 지원 만족도는 *양쪽* 극에서
>   떨어진다: 너무 디테일(마이크로매니징) **그리고** 너무 빈약(맥락 없는 제목만 티켓, 일부에게만 로드맵
>   공유, 너무 잦은 우선순위 변경). 건강대: 명확한 스프린트 목표+우선순위를 *전원*에게 공유, 과도한
>   변경 없이. 불명확한 스프린트 목표는 일관되게 플래닝 1위 방해요소, 계획외 고우선 유입·우선순위
>   churn은 실행 1위 방해요소다.
> - **구조적 버퍼를 두지 않으면 만성 오버페이스.** 플래닝 버퍼가 없으면 업무가 다음 스프린트로 밀리고
>   팀은 상시 오버페이스에 산다. 명시적 버퍼를 두고, 새 업무 유입 시 PM이 우선순위 재조정·descoping을
>   *주도*하라(조용히 쌓이게 두지 말 것).
> - **~10인 초과면 스크럼을 나누고, 회고가 나선을 닫게 하라 — 아니면 연극이다.** ~10인 넘으면 분할하라
>   (<15 던바 케이던스와 호응); "2주마다 KPT 왜?"라는 의구심이 나오면 나선이 안 닫히는 것이다. 서로의
>   배움을 축하하고 *지난번 개선을 추적*하는 것을 프로세스의 명시적 일부로 만들고 — 리더는 마이크로매니징에서
>   벗어나야 한다.

---

## 8. Introducing agile / a process transition (애자일·프로세스 전이 도입)

When asked to introduce scrum/agile (or any big process change), design the *adoption arc*, not a
big-bang switch. Empirically, a transition matures in a predictable order — and the early signals
look nothing like the steady-state ones.

- **Stage the rollout; effects compound.** Pilot on one project, then propagate team-wide — don't
  flip everyone at once. Each stage compounds on the last (in the data: post-coaching throughput
  rose multi-fold, then team-wide propagation added another step on top).
- **The first ROI is *visibility*, not speed.** The first and largest effect of adoption is that
  work becomes *visible and measurable* — throughput gains follow that, they don't lead it. Don't
  promise a velocity jump in month one; promise that you'll be able to *see* the work.
- **Maturation order: visibility → scope predictability → completion predictability.** Over-commit
  (e.g., ~111% scope estimate) calibrates toward ~100% first; final-completion predictability lags
  and stays stuck until you control mid-sprint additions and spec changes (rule #12). Sequence your
  expectations this way.
- **Estimates *deflate* toward the true unit as skill rises — read it as maturation, not slowdown.**
  Per-head SP drifts down toward ~1.0 SP/MD (the real unit) while *confidence rises*. Falling raw SP
  + rising confidence = calibration, not a productivity drop (links rule #9 / coaching Q15).
- **Correlation builds unevenly — some role-pairs are structurally phase-lagged, not broken.**
  Cross-role sync forms gradually and not for all pairs at once; a persistently low PM↔BE
  correlation is usually the planning-vs-build lifecycle gap, not a silo. Don't "fix" a pair that is
  just phase-shifted (refines rules #10, #16).

> **Caveat.** Transition measurement is assumption-laden (units shift, baselines move) — read
> *trends and direction*, not absolute precision. The source data itself flags it is not 100%
> reliable.

> **KO.** 스크럼/애자일(혹은 큰 프로세스 변경) 도입 요청을 받으면, 빅뱅 전환이 아니라 *도입 아크*를
> 설계하라. 전이는 예측 가능한 순서로 익으며, 초기 신호는 안정상태 신호와 전혀 다르게 보인다.
> - **단계적 롤아웃 — 효과는 복리.** 한 프로젝트에 파일럿 → 팀 전체로 전파, 한 번에 다 뒤집지 마라.
>   각 단계가 직전 위에 누적된다(데이터: 코칭 후 처리량 수배 상승 → 팀 전파가 그 위에 한 단계 더).
> - **첫 ROI는 속도 아닌 *가시성*.** 도입의 첫·최대 효과는 업무가 *보이고 측정되는* 것 — 처리량 향상은
>   그 뒤를 따르지 앞서지 않는다. 첫 달에 velocity 급등을 약속하지 말고, 업무가 *보이게* 됨을 약속하라.
> - **성숙 순서: 가시성 → 스코프 예측도 → 종료 예측도.** 과커밋(예: ~111% 스코프 추정)이 ~100%로 먼저
>   보정되고, 최종 종료 예측도는 지체되며 중간 추가·스펙 변경을 통제하기 전까진 정체한다(규칙 #12). 기대치를
>   이 순서로 깔아라.
> - **추정치는 스킬↑에 따라 진짜 단위로 *디플레이션* — 둔화가 아니라 성숙으로 읽어라.** 인당 SP가 ~1.0
>   SP/MD(진짜 단위)로 내려가는데 *자신감은 오른다.* 떨어지는 raw SP + 오르는 자신감 = 보정이지 생산성
>   하락이 아니다(규칙 #9 / 코칭 Q15 연결).
> - **상관은 불균등하게 형성 — 일부 직군쌍은 구조적 위상차이지 단절이 아니다.** 교차역할 싱크는 점진적·
>   비동시적으로 생긴다; 지속적으로 낮은 PM↔BE 상관은 보통 기획-개발 라이프사이클 시점차이지 사일로가
>   아니다. 위상만 어긋난 쌍을 "고치려" 들지 마라(규칙 #10·#16 보강).
>
> **단서.** 전이 측정은 가정이 많다(단위가 바뀌고 베이스라인이 이동) — 절대 정밀도가 아니라 *추세·방향*으로
> 읽어라. 원본 데이터 자체가 100% 신뢰도가 아님을 명시한다.

**Two named change-management models to run alongside the adoption arc.** The arc above tells
you the *maturation order*; these tell you how to *carry the people through it* — especially
apt for the AI-tooling adoption and team-merge scenarios this skill already covers.

- **Kotter's 8 steps (org level).** A sequence for institutional change: create **urgency** →
  build a **guiding coalition** → form the **vision** → **communicate** it → **enable action**
  (remove obstacles) → engineer **short-term wins** → **consolidate** gains → **anchor** it in
  the culture. Use it to sequence the *organization's* move.
- **ADKAR (individual level, Prosci).** Each affected person must clear five gates in order:
  **Awareness** (why) → **Desire** (want to) → **Knowledge** (how) → **Ability** (can do it)
  → **Reinforcement** (keeps doing it). A change stalls at whichever gate the individual is
  stuck behind — and people are stuck at *different* gates.

**Move: pair a Kotter org-level sequence with an ADKAR check on each affected person** — ask
where each one is stuck (still no **awareness**? has desire but no **ability**?) and aim the
help at *that* gate, not a one-size broadcast. (Provenance: Kotter; Prosci/ADKAR.)

> **KO.** **도입 아크와 나란히 돌릴 두 개의 변화관리 모델.** 위 아크는 *성숙 순서*를 알려주고,
> 이 둘은 그 위로 *사람을 어떻게 데려가나*를 알려준다 — 이 스킬이 이미 다루는 AI 도구 도입·팀 병합
> 시나리오에 특히 적합하다.
> - **코터 8단계(조직 수준).** 제도적 변화의 순서: **위기감** 조성 → **추진 연합** 구축 →
>   **비전** 수립 → **소통** → **행동 가능화**(장애물 제거) → **단기 성과** 설계 → 성과 **공고화**
>   → 문화에 **정착**. *조직*의 이동을 이 순서로 깔아라.
> - **ADKAR(개인 수준, 프로사이).** 영향받는 각 개인은 다섯 관문을 순서대로 통과해야 한다:
>   **인식**(왜) → **욕구**(하고 싶음) → **지식**(방법) → **능력**(할 수 있음) → **강화**(계속함).
>   변화는 그 개인이 막힌 관문에서 멈추며 — 사람마다 막힌 관문이 *다르다*.
>
> **무브: 코터 조직 수준 시퀀스에 영향받는 사람별 ADKAR 점검을 짝지어라** — 각자가 어디서 막혔는지
> 물어라(아직 **인식**이 없나? 욕구는 있는데 **능력**이 없나?) 그리고 도움을 *그 관문*에 겨눠라,
> 일괄 방송이 아니라. (출처: 코터; 프로사이/ADKAR.)

---

## 9. Managing up — the third axis (위로 관리하기 — 세 번째 축)

The skill's third axis (lead down · **manage up** · deliver) needs a method, not just a promise.
The core one is **Cognitive Alignment (thought-replication):** over ~2–8 weeks, build a working
replica of the decision-maker's/executives' thinking model — what they optimize for, what they
fear, how they weigh trade-offs — until you can *predict their call* and pre-frame proposals in
their language. The PM then acts as the **interpreter** between team and management, keeping an
appropriate distance from both and never turning psychologically negative on either side (management
usually has its own constraints too). (세 번째 축[아래로 이끌기·**위로 관리**·딜리버리]엔 약속이
아니라 방법이 필요하다. 핵심은 **인지 정렬(사고 복제)** — ~2~8주에 걸쳐 의사결정자·경영진의 사고
모델[무엇을 최적화·무엇을 두려워·트레이드오프 가중]을 복제해 *그들의 결정을 예측*하고 그들의 언어로
제안을 선프레이밍한다. PM은 팀↔경영진의 **통역사**로, 양쪽에 적정 거리를 두고 어느 쪽에도 심리적으로
부정적이 되지 않는다 — 경영진도 사정이 있다. Q17·Q44.)

**Two stakeholder lenses, complementary.** (1) the standard **Power / Interest 2×2** for external
stakeholders; (2) the author's **internal-team reading axes** for people inside the team — voice /
influence power, cooperation skill, self-management level, ability, tenure — a richer lens than
Power/Interest for the people you actually run with. Build the map *per team*. (스테이크홀더 렌즈
둘: 외부는 **Power/Interest 2×2**, 내부 팀원은 **저자의 내부 읽기 축**[voice/영향력·협업 스킬·자기관리
레벨·ability·연차] — 함께 일하는 사람에겐 Power/Interest보다 풍부한 렌즈. 팀별로 맵을 그려라. Q7·Q13.)

**Reporting *is* managing up.** Pre-agree the **RAG thresholds** with management so an escalation is
never a surprise; report to DACI on cadence (weekly, or biweekly for lower-interest parties);
escalate slips fast; and the moment a decision or milestone lands, disclose it immediately (loud
celebration for a hit, a sober "to teams" note for a miss). For high-interest management, a 15–30
min biweekly sync builds trust *and* speeds decisions. (보고가 곧 위로 관리다. **RAG 임계를 경영진과
사전 합의**해 에스컬레이션이 놀람이 되지 않게; DACI에 케이던스로 보고[주간, 관심 낮으면 격주]; 지연은
빠르게 에스컬레이션; 결정·마일스톤은 즉시 공개[달성=떠들썩한 축하, 미달=담담한 "to teams" 메시지].
관심 높은 경영진엔 격주 15~30분 싱크가 신뢰와 빠른 결정을 동시에. Q13·Q44.)

*The move:* don't translate up reactively — build the decision-maker's thought-replica so you can
pre-align proposals, and pre-agree RAG thresholds so escalation is routine, not alarm. (반응적으로
통역하지 말고 — 의사결정자의 사고 복제본을 만들어 제안을 선정렬하고, RAG 임계를 사전 합의해
에스컬레이션을 경보가 아닌 루틴으로.)

---

## 10. People — motivation, candor & conflict (사람 — 동기·솔직함·갈등)

**Motivation: fix hygiene before reaching for motivators.** Across the motivation theories
(Maslow / Herzberg / McClelland / Vroom / Adams), the operational order is Herzberg's: **hygiene
factors** (fair pay, environment, basic process, fairness) don't motivate — but their *absence*
demotivates and swamps everything else. So in a motivation 1:1, clear the hygiene blockers first;
only then do **motivators** (growth, recognition, autonomy, purpose, mastery) actually land. Don't
offer a growth narrative to someone sitting on an unfair-pay or broken-process grievance. (동기:
**위생요인을 먼저 고치고 동기요인으로.** 동기이론들[매슬로/허즈버그/맥클렐랜드/브룸/아담스]의 운영
순서는 허즈버그식 — **위생요인**[공정 보상·환경·기본 프로세스·공정성]은 동기를 *주지* 않지만 *부재*는
탈동기시키고 나머지를 다 덮는다. 동기 1:1에선 위생 블로커를 먼저 치우고, 그 다음에야 **동기요인**[성장·
인정·자율·목적·숙련]이 먹힌다. 불공정 보상·깨진 프로세스 불만 위에 성장 서사를 얹지 마라. Q24.)

**Dan Pink reframe — the motivators can't be *given*, only *enabled*.** Autonomy / mastery /
purpose are **intrinsic**: unlike hygiene factors, you cannot hand them over like a perk — you
can only **remove what blocks them** (per 무위: lift the interference and the drive surfaces on
its own). **Move: to lift motivation, don't pile extrinsic rewards on top of broken autonomy —
remove what blocks autonomy / mastery / purpose first.** (댄 핑크 리프레임 — 동기요인은 *줄* 수
없고 *가능하게 할* 수만 있다. 자율·숙련·목적은 **내재적**이다: 위생요인과 달리 복지처럼 건넬 수 없고,
**그것을 막는 것을 치울** 수 있을 뿐이다[무위: 간섭을 걷어내면 동기가 스스로 떠오른다]. 무브: 동기를
올리려면 깨진 자율 위에 외재적 보상을 쌓지 말고, 자율·숙련·목적을 막는 것을 먼저 치워라.)

**Radical candor needs its preconditions, or it reads as attack.** Kim Scott's two axes are *care
personally* × *challenge directly*; radical candor is high on both — feedback sharp enough to sting,
aimed at the person's growth. It only lands as growth (not as an attack) when the receiver **trusts**
the feedback helps them — which requires high personal care, psychological safety, and the receiver's
own belief "if I accept this, I grow." Build that trust substrate *first*; deployed into low safety,
the same words are just an uncomfortable attack. When it works, team and product gain a compounding
growth engine. This is the source of the skill's **dry-but-kind** register: sting where needed,
while standing with the person. (radical candor는 전제조건이 없으면 공격으로 읽힌다. 김 스콧의 두 축은
*개인적 관심* × *직접적 도전* — 둘 다 높은 게 radical candor, 따끔할 만큼 날카롭되 성장을 겨냥한 피드백.
받는 사람이 그 피드백이 자신에게 도움이 된다고 **신뢰**할 때만 공격이 아니라 성장으로 안착한다 — 높은
개인적 관심·심리적 안전감·"받아들이면 성장한다"는 본인의 믿음이 필요. 신뢰 토대를 *먼저* 쌓아라; 낮은
안전감에 꽂으면 같은 말이 불편한 공격일 뿐. 작동하면 팀·제품이 복리 성장 엔진을 얻는다. 이것이 스킬의
**드라이하되 친절한** 어투의 출처 — 따끔하되 곁에 선다. Q26.)

**Radical Candor — the four quadrants (complete the model).** The two axes (care personally ×
challenge directly) make four registers, and only one is the goal:

- **Radical Candor** — care **and** challenge. The target.
- **Ruinous Empathy** — care, **no** challenge. You stay silent to spare feelings, and the
  person never gets the truth they needed to grow. **This is the trap of a "kind" register** —
  the dry-but-kind warmth this skill prizes must NOT slide into withholding the hard truth.
  When you catch yourself being "nice" by staying quiet, **name it as ruinous empathy** and say
  the hard thing kindly.
- **Obnoxious Aggression** — challenge, no care. Sharp truth with no person behind it.
- **Manipulative Insincerity** — neither. The worst quadrant: false praise, politics.

Kim Scott's loop to *get* candor flowing, in order: **Get** feedback first (solicit criticism
on yourself), **Give** both praise and criticism, **Encourage** it between others, **Gauge**
how each person receives it. **Move: solicit criticism on yourself before you give any; and if
you're staying silent to be "nice," name it as ruinous empathy and say the hard thing kindly.**

> **KO.** **radical candor의 네 사분면(모델 완성).** 두 축(개인적 관심 × 직접적 도전)이 네 어투를
> 만들고, 목표는 하나뿐이다: **Radical Candor**(관심+도전 — 목표), **Ruinous Empathy**(관심 있고
> 도전 없음 — 감정을 아끼려 침묵해 상대가 성장에 필요한 진실을 못 받음. **이것이 "친절한" 어투의 함정** —
> 이 스킬이 아끼는 드라이하되-친절한 따뜻함이 결코 어려운 진실을 보류하는 쪽으로 미끄러지면 안 된다. 침묵으로
> "착하게" 굴고 있는 자신을 잡으면 **루이너스 엠퍼시라 명명**하고 어려운 말을 친절하게 하라),
> **Obnoxious Aggression**(도전 있고 관심 없음 — 사람이 빠진 날 선 진실), **Manipulative Insincerity**
> (둘 다 없음 — 거짓 칭찬·정치, 최악). 김 스콧의 캔더를 *흐르게* 하는 루프, 순서대로: 먼저 **Get**(자신에
> 대한 비판을 구함) → **Give**(칭찬과 비판 둘 다) → **Encourage**(타인들 사이에 권장) → **Gauge**(각자가
> 어떻게 받아들이는지 가늠). **무브: 주기 전에 먼저 자신에 대한 비판을 구하라; "착하게" 굴려 침묵하고 있다면
> 루이너스 엠퍼시라 명명하고 어려운 말을 친절하게 하라.**)

**SBI — the exact words for a piece of candor.** The skill knows *why* and *when* to be candid;
SBI is the *sentence shape*. State **Situation → Behavior → Impact**, factually, without a
character verdict: *"in yesterday's standup (S), you cut Mina off twice (B), and she stopped
offering estimates (I)."* Then give a **feedforward** — one concrete future move — instead of
relitigating the past: *"next standup, hold your point until the speaker finishes."* **Move:
deliver every piece of candor as SBI + one feedforward.**

> **KO.** **SBI — 캔더의 정확한 문장 형태.** 스킬은 *왜·언제* 솔직할지를 알지만 SBI는 그 *문장
> 모양*이다. 인격 평결 없이 사실로 **상황 → 행동 → 영향**을 말하라: *"어제 스탠드업에서(S) 미나의 말을
> 두 번 끊었고(B), 그 뒤로 미나가 추정치를 내놓지 않더라(I)."* 그리고 과거를 다시 따지는 대신
> **피드포워드** — 하나의 구체적 미래 무브 — 를 줘라: *"다음 스탠드업엔 발언자가 끝낼 때까지 네 요점을
> 잡고 있어 줘."* **무브: 모든 캔더를 SBI + 피드포워드 하나로 전하라.**)

**Conflict — pick the mode on purpose, and make it safe first.** Candor handles the *one-way*
hard message; conflict is *two* parties with a clash, and it needs its own model.

- **Thomas–Kilmann — five modes on assertiveness × cooperativeness:** **competing**
  (assertive, uncooperative), **collaborating** (both high), **compromising** (middle),
  **avoiding** (both low), **accommodating** (cooperative, unassertive). No mode is "best" —
  **match the mode to the situation:** collaborate for high-stakes / high-trust clashes;
  compromise under time pressure; avoid the trivial; accommodate when you're wrong or it
  matters far more to them; compete only on non-negotiables (safety, ethics). Most people
  over-default to one mode — choose deliberately.
- **Crucial Conversations — when stakes and emotions are high, *first make it safe*.** Before
  arguing content, restore **mutual respect and mutual purpose** — people only think clearly
  inside safety. Then **STATE** your path: **S**hare your facts, **T**ell your story,
  **A**sk for theirs — to grow a *pool of shared meaning* rather than two competing monologues.
  Frame "make it safe" through 측은(care for the person across the table) + 중정(holding the
  balance, not winning) + **proximity** (in friction, get closer — §5).

**Move: before a hard conversation, pick the Thomas–Kilmann mode on purpose, and make it safe
(restore respect + shared purpose) before you state your view.**

> **KO.** **갈등 — 모드를 의도적으로 고르고, 먼저 안전하게 만들어라.** 캔더는 *일방향* 어려운
> 메시지를 다루고, 갈등은 부딪치는 *두* 당사자라 별도 모델이 필요하다.
> - **토마스-킬만 — 주장성 × 협조성 위의 다섯 모드:** **경쟁**(주장↑·협조↓), **협력**(둘 다 높음),
>   **타협**(중간), **회피**(둘 다 낮음), **수용**(협조↑·주장↓). "최선"의 모드는 없다 — **상황에
>   모드를 맞춰라:** 고위험·고신뢰 충돌엔 협력, 시간 압박엔 타협, 사소한 건 회피, 내가 틀렸거나
>   상대에게 훨씬 더 중요하면 수용, 협상 불가(안전·윤리)에만 경쟁. 대부분 한 모드로 기본값이
>   치우치니 — 의도적으로 골라라.
> - **결정적 순간 — 위험·감정이 높을 땐 *먼저 안전하게*.** 내용을 다투기 전에 **상호 존중과 공동
>   목적**을 회복하라 — 사람은 안전 안에서만 명료히 생각한다. 그다음 **STATE**로 길을 펴라: 사실을
>   **공유**하고, 내 이야기를 **말하고**, 상대 이야기를 **물어라** — 두 개의 경쟁 독백이 아니라
>   *공유된 의미의 풀*을 키우려. "안전하게 만들기"는 측은(맞은편 사람에 대한 케어) + 중정(이기는 게
>   아니라 균형을 쥠) + **근접성**(마찰엔 가까이 — §5)으로 프레이밍하라.
>
> **무브: 어려운 대화 전에 토마스-킬만 모드를 의도적으로 고르고, 내 견해를 펴기 전에 먼저 안전하게
> 만들어라(존중 + 공동 목적 회복).**

> Both rest on **self-management as the root of trust:** a person who can't manage themselves earns
> only fake trust, so autonomy and candor are extended as that root grows (the minute-level loop in
> §2; rule #7; coaching Q25). (둘 다 **자기관리 = 신뢰의 뿌리** 위에 선다 — 스스로를 관리 못 하는
> 사람은 가짜 신뢰만 얻으니, 그 뿌리가 자랄수록 자율·솔직함을 확장한다. §2 분 단위 루프·규칙 #7·코칭 Q25.)
