# 얼라인드 딜리버리 (Aligned Delivery)

> **PM 코칭 + 팀 딜리버리 진단 + 피드백 루프 설계** 를 위한 설치형 Claude 스킬 — 실제로 동작하는
> 분석 스크립트와 평가 세트로 뒷받침됩니다. 영어/한국어 이중언어로 동작합니다.

> 🌐 English version → [README.md](README.md)

> **버전: 0.1.0** — [CHANGELOG.md](CHANGELOG.md) 참고.

---

## 무엇을 하는가

얼라인드 딜리버리는 Claude 에이전트가 **PM 코치 + 팀 운영 진단가 + 피드백 루프 설계자** 로
동작하게 하고, 모든 행동을 측정으로 뒷받침합니다.

세 가지 역량:

- **A. PM 코칭·인터뷰** — 레벨링된 12개 카테고리, **49문항**. 팀을 이끌고·키우기, 경영진/
  스테이크홀더 관리(managing up), 자기관리까지 다룹니다. 검증된 프레임워크에 근거합니다:
  **Radical Candor**, **Thomas-Kilmann** 갈등 모드, **Team Topologies / Conway 법칙**,
  **DORA**, **Lean / Build-Measure-Learn**. → `references/coaching-questions.md`
- **B. 팀 딜리버리 진단** — 헬스체크 + 1:1 "보정(correction)", 그리고 스프린트/지라 분석을
  **5개의 동작하는 표준 라이브러리 파이썬 스크립트** 로 수행: 스프린트 예측도, 헬스체크,
  업무량/사일로 분석, **SP 불요 DORA 플로우 지표**, **몬테카를로** 딜리버리 예측.
  ([스크립트](#스크립트) 참고.)
- **C. 피드백 루프·의식 설계** — 스프린트 케이던스, KPT 회고, 컨피던스 레벨 추적, RAG 플래그,
  **우선순위(WSJF / Cost of Delay / RICE)**, 그리고 최소 간섭(무위) 가드레일.

**무엇이 다른가:** 단순히 의견을 가진 게 아니라 — **동작하는 스크립트 + 측정 가능한 평가** 를
함께 제공합니다. `evals/` 세트는 세 역량을 고정 프롬프트와 기대 동작에 대해 실행하므로, 스킬을
켰을 때의 출력을 끄고 낸 베이스라인과 비교할 수 있습니다. (It ships working scripts plus a
measured eval, so you can compare with-skill output against an unguided baseline.)

**대상이 아닌 것:** 일반 HR/연봉, 채용 실무, 개인 커리어 조언, 피치덱 / 고투마켓 / 사업 전략,
순수 코딩. (Not for: generic HR/comp, hiring logistics, individual career advice, pitch decks /
go-to-market / business strategy, or pure coding.)

## 스크립트

파이썬 표준 라이브러리만 사용합니다(pandas 없음). 본인의 스프린트/설문 CSV에 바로 실행하세요.

```bash
python3 scripts/sprint_predictability.py  your_sprints.csv     # 스코프·완료 예측도, 업무량 표준편차, RAG
python3 scripts/health_check_analyze.py    your_survey.csv      # 평균·델타·플래그, 1:1 "보정" 워크시트
python3 scripts/workload_fragmentation.py  your_workload.csv    # 파편화 지수, 교차 역할 상관, 운영 비중, 사일로 위험
python3 scripts/flow_metrics.py            your_flow.csv        # SP 불요 DORA 4대 지표: 처리량·리드/사이클타임·플로우 효율 + 배포 빈도·변경 실패율·MTTR
python3 scripts/forecast_montecarlo.py     your_throughput.csv --backlog 50   # #NoEstimates 몬테카를로 예측: 과거 처리량에서 P50/P85/P95 완료 기간
```

각 스크립트에는 `--help` 와 샘플 CSV가 함께 있습니다(`evals/sprints.csv`,
`scripts/sample_health_check.csv`, `scripts/sample_workload.csv`, `scripts/sample_flow.csv`,
`scripts/sample_throughput.csv`).

### 바로 실행 (Try it)

함께 제공된 샘플로 바로 동작합니다(정상 동작 확인됨):

```bash
python3 scripts/sprint_predictability.py evals/sprints.csv
python3 scripts/flow_metrics.py scripts/sample_flow.csv
python3 scripts/forecast_montecarlo.py scripts/sample_throughput.csv --backlog 50
```

또는 스프린트 CSV와 함께 Claude에게 *"우리 생산성 괜찮나요?"* 라고 물으면 →
`sprint_predictability` 를 실행하고 **스코프 예측도를 먼저** 읽어(선행 지표) 가짜 생산성을
짚어냅니다. (Ask *"Is our productivity healthy?"* with a sprint CSV → it runs
`sprint_predictability`, reads scope predictability first, and flags fake productivity.)

## 그 뒤의 렌즈 — 철학

위 기능만으로도 스킬은 충분히 동작합니다. 이 절은 그 뒤의 조직 원리이며, 원하는 만큼 들어가면
됩니다(opt-in). (The skill works on its own merits above; this section is the organizing lens.)

**한 줄 명제:** *신념은 성과 아래의 하중층이고, **정렬(alignment)** — 정답이 아니라 — 이 안정성을
만들며, 진짜 생산성은 영웅적 속도가 아니라 안정성에서 나옵니다.*

**쉽게 말해:** 이 방법론은 팀을 **세 층위의 공명 시스템 — 잠재 구조(리), 살아 있는 상태(기),
측정 가능한 흔적(도)** — 으로 읽고, **최소 간섭** 으로 팀이 스스로 정렬하도록 이끕니다. (Reads a
team as a resonant system on three layers — latent structure (리), live state (기), measurable
trace (도) — and leads by minimal interference.)

이 렌즈는 **N2C(네오² 유학 / 동적 공명 존재론)** 에 근거합니다. 팀을 고정된 기계가 아니라
**공명하는 궤적(resonant trajectory)** 으로 읽고, **응축 → 해산 → 창발 → 무위** 로 움직입니다.
9개 운영 원칙은 `references/principles.md` 를 참고하세요.

**선택적 동반 스킬 — `life-reading` (선택).** 의사결정·판단 요청 시 형제 스킬 **`life-reading`** 를 답변 뒤에서
**0-impact 공명 보완** 으로 *선택적* 실행합니다 — 필수가 아니라 옵션입니다. 미설치 시
`references/principles.md` 의 리·기·도 렌즈로 폴백하고 정상 진행합니다. (On decision/judgment
requests this optionally runs the sibling `life-reading` as a 0-impact resonance complement; it is opt-in,
not required, and falls back to the 리·기·도 lens if `life-reading` isn't installed.)

## 설치

**Claude Code / Cowork:** 스킬 디렉터리에 복제(또는 복사)하면, PM 코칭·팀 진단·루프 설계 관련
요청을 할 때 — 영어든 한국어든 — 스킬이 자동으로 발동됩니다.

```bash
git clone https://github.com/ahnbingbing/aligned-delivery.git ~/.claude/skills/aligned-delivery
```

또는 패키징된 `.skill` 파일을 공유해도 됩니다(skill-creator의 `package_skill.py` 로 생성).

## 저장소 구조

```
aligned-delivery/
├── SKILL.md                     # 진입점: 리·기·도 렌즈, 역량 라우터, 응답 방식
├── references/
│   ├── principles.md            # N2C 근거: 리·기·도 렌즈 + 9개 원칙
│   ├── operating-loops.md       # 사이클 + 무위 리더십; 케이던스·헬스체크·회고·루프 설계
│   ├── operating-rules.md       # 경험칙 — 우선순위(Cost of Delay / WSJF / RICE), DORA 속도+안정성, DACI/타임박스 결정 규칙(규칙 #24–29)까지
│   ├── coaching-questions.md    # 12개 카테고리, 49문항 레벨링 PM 프레임워크
│   └── manifesto.md             # EN/KO 어조가 따르는 소스 보이스 선언문
├── scripts/                     # 동작하는 분석 스크립트 5종(표준 라이브러리만; SP-free DORA 플로우 지표 + 몬테카를로 예측 포함)
├── assets/                      # 헬스체크 / KPT 회고 / 스프린트 리포트 템플릿
└── evals/                       # 테스트 케이스 3개 + 샘플 sprints.csv
```

## 크레딧·라이선스

지적 근간은 **N2C — 네오² 유학 / 동적 공명 존재론** (리·기·도, 파동, 공조층; 불확정성 × 근접성)
이며, 스킬이 철학 *자체* 라고 과장하지 않으면서 팀 운영에 적용합니다. 운영 경험칙은 실제 프로덕트
팀 데이터에서 일반화한 것입니다(회사·프로젝트명 없음, 비율 외 독점 수치 없음).

**MIT 라이선스** 로 배포됩니다 — [`LICENSE`](LICENSE) 참고. © 2026 Yuri Ahn.

---

피드백·이슈 → https://github.com/ahnbingbing/aligned-delivery/issues
