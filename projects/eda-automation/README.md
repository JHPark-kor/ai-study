# DataPrep Studio 실행 방법·코드

[메인으로 돌아가기](../../README.md#사이드-프로젝트) · [실제 코드 다운로드 · ZIP](files/DataPrep-Studio-Team-Share-2026-09-28.zip)

## 다운로드

[DataPrep Studio Windows용 소스 ZIP · 2026-09-28](files/DataPrep-Studio-Team-Share-2026-09-28.zip)

ZIP을 풀면 실행 스크립트, 소스 코드, 테스트와 합성 예제가 들어 있는 `DataPrep-Studio` 폴더가 나옵니다. Python·PostgreSQL·Codex는 먼저 설치해야 합니다.

## 준비 환경

- Windows 10/11
- Python 3.11 이상, PostgreSQL
- Codex 앱 또는 CLI와 본인의 ChatGPT 계정

## 처음 실행하기

1. ZIP을 풀고 `DataPrep-Studio` 폴더를 엽니다.
2. `setup.ps1`을 실행해 가상환경과 Python 패키지를 설치합니다.
3. PostgreSQL을 실행하고 빈 데이터베이스를 만든 뒤, 생성된 `.env`에 본인 PC의 연결 정보를 입력합니다.
4. `환경확인.cmd`로 PostgreSQL과 Codex 연결 상태를 확인합니다.
5. `시작.cmd`를 실행합니다. 브라우저가 열리지 않으면 `http://127.0.0.1:8502`에 접속합니다.
6. 화면의 **연결 설정 → ChatGPT로 로그인**에서 본인 계정으로 인증합니다.

PowerShell에서 설치 스크립트를 실행하려면 해당 폴더에서 다음 명령을 사용합니다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
```

API 키를 입력하거나 공유하지 않습니다. 이후에는 PostgreSQL을 실행한 상태에서 `시작.cmd`로 열고, 작업을 마치면 `종료.cmd`로 닫습니다.

## 사용 흐름

파일·분석 목적 입력 → 데이터 개요·변수 진단 → 질문·답변 → 변경 미리보기 → 검토·승인 → 새 버전 적용 → 결과 다운로드

CSV·Excel(.xlsx)·TXT·TSV·dense ARFF·일반 UEA/UCR TS와 ZIP 내부 파일 하나를 입력할 수 있습니다. 처리 판단을 보류하고 원본 진단 결과만 받을 수도 있습니다.

| 받는 결과 | 형식 |
|---|---|
| 데이터 테이블·메타데이터 사전 | CSV, 사전 HTML |
| 전처리 분석 보고서 초안 | HTML |
| 진단·승인된 정제의 재현 코드 | IPYNB |
| 보고서·사전·데이터·노트북·원본·처리 명세 | 전체 ZIP |

## 작동 방식

Python이 통계·분포·품질 검사와 정제를 수행하고, Agent AI(Codex)가 계산 결과·목적·메타데이터를 바탕으로 설명과 질문, 정제 후보를 제시합니다. 실제 변경은 사용자가 영향을 확인하고 승인한 규칙만 원본을 보존한 새 버전에 적용합니다.

원본·결과 파일은 로컬에, 작업 상태·결정·버전과 파일 참조는 PostgreSQL에 저장합니다. 각자의 PC와 계정을 사용하며 분석 이력이 자동으로 다른 팀원에게 공유되지는 않습니다.

## 코드 구조

압축을 푼 `DataPrep-Studio` 폴더 기준입니다.

| 코드 | 역할 |
|---|---|
| `app.py`, `studio/styles.py` | 입력·진단·대화·승인을 연결하는 화면 |
| `worker.py` | 화면과 분리된 진단·대화 작업 |
| `studio/analysis_loader.py`, `studio/analysis.py` | 파일 읽기·통계·변수 진단 |
| `studio/ai.py`, `studio/codex_client.py` | 목적 기반 해석·질문·Codex 연결 |
| `studio/service.py`, `studio/cleaning.py` | 답변 반영·미리보기·승인·정제·버전 관리 |
| `studio/repository.py` | PostgreSQL 상태·결정 이력 저장 |
| `studio/exports.py` | HTML 보고서·사전·CSV·노트북·ZIP 생성 |
| `setup.ps1`, `start.ps1`, `stop.ps1` | 환경 준비·실행·종료 |
| `specs/001-team-prototype/`, `tests/` | 요구사항·설계와 기능 테스트 |

ZIP 안의 `TEAM_SETUP.md`와 `DEVELOPMENT.md`에서 설치 및 개발 세부 사항을 확인할 수 있습니다.

[메인으로 돌아가기](../../README.md#사이드-프로젝트) · [코드 ZIP 다운로드](files/DataPrep-Studio-Team-Share-2026-09-28.zip)
