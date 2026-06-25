# Aligned Delivery (얼라인드 딜리버리)

> An installable Claude skill for **PM coaching + team-delivery diagnostics + feedback-loop
> design** — backed by real, runnable analytics scripts and an eval suite. Bilingual EN / KO.
>
> **PM 코칭 + 팀 딜리버리 진단 + 피드백 루프 설계** 를 위한 설치형 Claude 스킬 — 실제로 동작하는
> 분석 스크립트와 평가 세트로 뒷받침됩니다. 영어/한국어 이중언어.

> 🌐 한국어 버전 → [README.ko.md](README.ko.md)

> **Version: 0.1.0** — see [CHANGELOG.md](CHANGELOG.md).

---

## What it does (무엇을 하는가)

Aligned Delivery lets a Claude agent act as a **PM coach + team-operations diagnostician +
feedback-loop designer**, and backs every move with measurement. (Claude 에이전트가 **PM 코치 +
팀 운영 진단가 + 피드백 루프 설계자** 로 동작하며, 모든 행동을 측정으로 뒷받침합니다.)

Three capabilities (세 역량):

- **A. PM coaching & interviewing (PM 코칭·인터뷰)** — a leveled, 12-category question framework
  (49 Q&As). Covers leading & developing a team, managing up to stakeholders/executives, and
  self-management. Grounded in known frameworks: **Radical Candor**, **Thomas-Kilmann** conflict
  modes, **Team Topologies / Conway's Law**, **DORA**, and **Lean / Build-Measure-Learn**.
  See `references/coaching-questions.md`.
- **B. Team-delivery diagnostics (팀 딜리버리 진단)** — health check + 1:1 "correction" plus
  sprint/Jira analytics, via **five working stdlib Python scripts**: sprint predictability,
  health-check, workload/silo analysis, **SP-free DORA flow metrics**, and **Monte Carlo**
  delivery forecasting. (See [The scripts](#the-scripts-스크립트).)
- **C. Feedback-loop & ceremony design (피드백 루프·의식 설계)** — sprint cadence, KPT retros,
  confidence-level tracking, RAG flags, **prioritization (WSJF / Cost of Delay / RICE)**, and
  minimal-interference guardrails.

**Why it's different:** it doesn't just hold opinions — it **ships working scripts plus a measured
eval**. The `evals/` suite runs the three capabilities against fixed prompts with expected
behavior, so you can compare with-skill output against an unguided baseline. (단순 의견이 아니라
**동작하는 스크립트 + 측정 가능한 평가**를 함께 제공합니다.)

**Not for:** generic HR/comp, hiring logistics, individual career advice, pitch decks /
go-to-market / business strategy, or pure coding. (일반 HR/연봉, 채용 실무, 개인 커리어 조언,
피치덱 / 고투마켓 / 사업 전략, 순수 코딩은 대상이 아닙니다.)

## The scripts (스크립트)

Stdlib-only Python (no pandas). Run them directly on your own sprint/survey CSVs. (파이썬 표준
라이브러리만 사용. 본인 CSV에 바로 실행.)

```bash
python3 scripts/sprint_predictability.py  your_sprints.csv     # scope/completion predictability, workload STDEV, RAG
python3 scripts/health_check_analyze.py    your_survey.csv      # averages, deltas, flags, 1:1 "correction" worksheet
python3 scripts/workload_fragmentation.py  your_workload.csv    # fragmentation index, cross-role correlation, ops ratio, silo risk
python3 scripts/flow_metrics.py            your_flow.csv        # SP-free DORA 4 keys: throughput, lead/cycle time, flow efficiency + deploy freq, change failure rate, MTTR
python3 scripts/forecast_montecarlo.py     your_throughput.csv --backlog 50   # #NoEstimates Monte Carlo forecast: P50/P85/P95 periods-to-done from history
```

Each has `--help` and a sample CSV alongside it (`evals/sprints.csv`,
`scripts/sample_health_check.csv`, `scripts/sample_workload.csv`, `scripts/sample_flow.csv`,
`scripts/sample_throughput.csv`).

### Try it (바로 실행)

Runs out of the box on the shipped samples (정상 동작 확인된 샘플):

```bash
python3 scripts/sprint_predictability.py evals/sprints.csv
python3 scripts/flow_metrics.py scripts/sample_flow.csv
python3 scripts/forecast_montecarlo.py scripts/sample_throughput.csv --backlog 50
```

Or just ask Claude *"Is our productivity healthy?"* with a sprint CSV → it runs
`sprint_predictability`, reads **scope predictability first** (the leading indicator), and flags
fake productivity. (또는 스프린트 CSV와 함께 *"우리 생산성 괜찮나요?"* 라고 물으면 →
`sprint_predictability` 를 실행하고 **스코프 예측도를 먼저** 읽어(선행 지표) 가짜 생산성을
짚어냅니다.)

## The lens behind it (philosophy) (그 뒤의 렌즈 — 철학)

The skill works on its own merits above; this section is the organizing lens, opt-in depth.
(위 기능만으로도 충분히 동작합니다. 이 절은 그 뒤의 조직 원리이며, 원하는 만큼 들어가면 됩니다.)

**One-line thesis:** *belief is the load-bearing layer under performance; **alignment** (not the
single right answer) creates stability; and real productivity comes from stability, not heroic
speed.* (신념은 성과 아래의 하중층이고, **정렬**(정답이 아닌)이 안정성을 만들며, 진짜 생산성은
영웅적 속도가 아니라 안정성에서 나옵니다.)

**In plain terms:** the method reads a team as a **resonant system on three layers — latent
structure (리), live state (기), and measurable trace (도)** — and leads by **minimal
interference** so the team self-aligns. (쉽게 말해, 팀을 세 층위의 공명 시스템 — 잠재 구조(리)·
살아 있는 상태(기)·측정 가능한 흔적(도) — 으로 읽고, **최소 간섭** 으로 스스로 정렬하게 이끕니다.)

This lens is grounded in **N2C (Neo²-Confucianism / Dynamic Resonance Ontology)**. It reads a team
not as a fixed machine but as a **resonant trajectory**, and moves it through
**응축 → 해산 → 창발 → 무위**. The nine operating principles are in `references/principles.md`.
(이 렌즈는 **N2C(네오² 유학 / 동적 공명 존재론)** 에 근거합니다. 팀을 고정된 기계가 아니라
**공명하는 궤적** 으로 읽고 응축→해산→창발→무위로 움직입니다. 9개 운영 원칙은
`references/principles.md` 참고.)

**Optional companion — `life-reading` (선택).** On decision/judgment requests this skill *optionally* runs
the sibling **`life-reading`** skill behind the answer as a **0-impact resonance complement**. It is opt-in
flavor, not a requirement: if `life-reading` isn't installed, the skill falls back to the 리·기·도 lens in
`references/principles.md` and proceeds normally. (의사결정·판단 요청 시 형제 스킬 `life-reading` 를 답변
뒤에서 **0-impact 공명 보완** 으로 *선택적* 실행합니다 — 필수가 아니라 옵션입니다. 미설치 시
`references/principles.md` 의 리·기·도 렌즈로 폴백하고 정상 진행합니다.)

## Install (설치)

**Claude Code / Cowork:** clone (or copy) into your skills directory, then the skill triggers
automatically when you ask PM-coaching / team-diagnosis / loop-design questions — in English or
Korean. (스킬 디렉터리에 복제·복사하면, PM 코칭·팀 진단·루프 설계 요청 시 영어/한국어로 자동
발동됩니다.)

```bash
git clone https://github.com/ahnbingbing/aligned-delivery.git ~/.claude/skills/aligned-delivery
```

Or share the packaged `.skill` file (built with skill-creator's `package_skill.py`). (또는
패키징된 `.skill` 파일 공유.)

## Repository layout (저장소 구조)

```
aligned-delivery/
├── SKILL.md                     # entry point: 리·기·도 lens, capability router, how-to-respond
├── references/
│   ├── principles.md            # N2C grounding: 리·기·도 lens + 9 principles
│   ├── operating-loops.md       # cycle + 무위 leadership; cadence, health check, retro, loop design
│   ├── operating-rules.md       # heuristics through prioritization (Cost of Delay / WSJF / RICE), DORA speed+stability, and DACI/timebox decision rules (rules #24–29)
│   ├── coaching-questions.md    # 12-category, 49-question leveled PM framework
│   └── manifesto.md             # source-voice declaration the EN/KO register draws from
├── scripts/                     # 5 working analytics scripts (stdlib only; incl. SP-free DORA flow metrics + Monte Carlo forecast)
├── assets/                      # health-check / KPT-retro / sprint-report templates
└── evals/                       # 3 test cases + sample sprints.csv
```

## Credits & license (크레딧·라이선스)

The intellectual backbone is **N2C — Neo²-Confucianism / Dynamic Resonance Ontology** (리·기·도,
wave, cooperation layer; unexpectancy × proximity), applied here to team operations without the
skill overclaiming to *be* a philosophy. Operating heuristics are generalized from real
product-team data (no company/project names, no proprietary figures beyond ratios). (지적 근간은
**N2C**이며, 팀 운영에 적용하되 스킬이 철학 *자체* 라고 과장하지 않습니다. 운영 경험칙은
실데이터에서 일반화한 것입니다.)

Licensed under the **MIT License** — see [`LICENSE`](LICENSE). © 2026 Yuri Ahn.

---

Feedback & issues → https://github.com/ahnbingbing/aligned-delivery/issues
