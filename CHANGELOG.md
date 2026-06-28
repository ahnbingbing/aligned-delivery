# Changelog

All notable changes to **Aligned Delivery** are documented here. Bilingual EN / KO.
This project adheres to [Semantic Versioning](https://semver.org/).

## 0.1.1

Output hygiene: **chat answers are now plain text — no markdown markup** (`**bold**`,
`#` headings), since a conversational reply is often read where markdown isn't rendered
(chat bot, Telegram, mobile) and shows up as literal `**`/`#`. Rich markdown (tables, `#`,
`**`) is **reserved for saved artifacts and contexts known to render it** — e.g. a
health-check/sprint report written from `assets/*template.md`, where tables belong. Mirrors
the sibling `life-reading` 0.1.1 plain-text fix. Enforced in `SKILL.md` (How to respond).

출력 위생: **채팅 답변은 평문 — 마크다운(`**`·`#`) 금지** (봇/텔레그램/모바일 등 렌더링 안
되는 곳에서 별표·샵이 그대로 보임). 표·`#`·굵게 같은 리치 마크다운은 **저장 산출물(.md
리포트)·렌더링 보장된 곳에서만**. 형제 `life-reading` 0.1.1 평문 수정과 동일한 결.

## 0.1.0

Initial build: an installable, bilingual (EN/KO) Claude skill that turns a belief-first
delivery philosophy (N2C — 리·기·도) into a working PM operating method — PM coaching/interview
framework (12 categories, 49 Q&As), team-operations diagnosis with five stdlib-only analytics
scripts (sprint predictability, health check, workload fragmentation, SP-free DORA flow metrics,
Monte Carlo forecast), and feedback-loop/ceremony design. Optional `life-reading` companion runs as a
0-impact resonance complement on decision requests, with a `principles.md` 리·기·도 fallback.

초기 빌드: 신념 우선 딜리버리 철학(N2C — 리·기·도)을 작동하는 PM 운영 방법론으로 바꾼
설치형·이중언어(EN/KO) Claude 스킬 — PM 코칭·인터뷰 프레임워크(12 카테고리, 49문항), 표준
라이브러리만 쓰는 분석 스크립트 5종(스프린트 예측도, 헬스체크, 업무량 파편화, SP 불요 DORA 플로우
지표, 몬테카를로 예측)으로 하는 팀 운영 진단, 피드백 루프·의식 설계. 의사결정 요청 시 형제 스킬
`life-reading` 를 0-impact 공명 보완으로 선택적 실행하며, 미설치 시 `principles.md` 의 리·기·도 렌즈로 폴백.
