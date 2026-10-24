# Bayesian · analysis

W11에는 베이지안 모델을 문화예술 관람 의향, 반도체 공정 불량, 신용카드 연체 데이터에 적용했다.
아래 기록은 2026-10-24에 확인한 [Notion W11 페이지](https://app.notion.com/p/3e9917c0e64080dea322cccd48b956c1)의 실제 첨부를 기준으로 한다. PDF와 노트북은 파일명만 정리하고 원본 내용은 그대로 보존했다.

| 스터디원 | 분석 보고서 | 노트북 | 확인된 범위 |
| --- | --- | --- | --- |
| 박중현 | [PDF](files/w11_bayesian_analysis_박중현.pdf) | 해당 Notion 페이지에 미첨부 | 분석 결과·가설 검정·결론 |
| 강재성 | [PDF](files/w11_bayesian_analysis_강재성.pdf) | [ipynb](files/w11_bayesian_analysis_강재성.ipynb) | 전처리·교차검증·최종 평가·해석 |
| 신정윤 | [PDF](files/w11_bayesian_analysis_신정윤.pdf) | [ipynb](files/w11_bayesian_analysis_신정윤.ipynb) | 전처리·구조 비교·조건부 확률표 학습 |

## 박중현 · 문화예술 관람 의향

- 국민문화예술활동조사 2023~2025년 자료를 통합해 뮤지컬 관람 의향과 문화자본·문화 접점의 관계를 살펴봤다.
- 성인 응답자 28,779명 중 결측 43행을 제외하고, PC 구조 탐색과 베이지안 네트워크 학습을 진행했다.
- 보고서의 평가 결과는 AUC 0.7570, Brier score 0.0928이며, 부트스트랩으로 변수군별 설명량 차이를 검토했다.
- 문화자본·문화 접점의 합산 설명량이 더 컸지만 직접관람 연결을 제외하면 차이가 뚜렷하지 않아, 해석의 민감성을 함께 남겼다.

[Notion 원문](https://app.notion.com/p/b3b917c0e640837e8882813aaf3fdd48) · [분석 보고서](files/w11_bayesian_analysis_박중현.pdf)

노트북은 해당 페이지와 이번 내보내기에 포함되지 않았다. 보고서의 수치와 분석 흐름은 확인했지만 코드 재현 여부는 확인하지 못했다.

## 강재성 · 반도체 공정 불량 분류

- SECOM의 생산 표본 1,567개를 이용해 Gaussian Naive Bayes로 양품과 불량을 구분했다.
- 학습 데이터에서 고결측·상수 변수를 제거하고 중앙값 대체·표준화를 적용했으며, 교차검증으로 `var_smoothing=0.5`를 선택했다.
- 테스트 불량 21개 중 14개를 검출하고 양품 90개를 오판했으며, 균형 정확도 0.6797과 ROC-AUC 0.7290은 보고서와 노트북의 저장 결과가 일치한다.
- 불량 누락과 추가 검사 부담을 함께 해석했고, 테스트 불량 수가 적어 생산 수율 개선이나 검사 대체 효과로 확대 해석하지 않았다.

[Notion 원문](https://app.notion.com/p/3ec917c0e64080bd902cc553329c6294) · [분석 보고서](files/w11_bayesian_analysis_강재성.pdf) · [노트북](files/w11_bayesian_analysis_강재성.ipynb)

같은 페이지의 [수학 발표 보조자료](files/w11_bayesian_analysis_supplement_math_강재성.pdf)는 세미 나이브 베이즈, 베이지안 네트워크, EM을 설명한다. 분석 결과 보고서와 구분해 W11 첨부로 보존하며, W9 수학 제출물에 중복 산정하지 않는다.

## 신정윤 · 신용카드 연체 예측 구조 설계

- UCI 신용카드 고객 30,000명의 자료로 다음 달 연체를 설명하는 베이지안 네트워크를 설계했다.
- 범주 재분류, 파생 변수 생성, 학습 데이터 기준 이산화를 거쳐 전문가 구조와 Hill Climbing의 BIC·K2 구조를 비교했다.
- 노트북에는 Naive Bayes를 포함한 구조별 MLE·라플라스 평활 확률표 학습과 모델 유효성 검사 결과가 저장되어 있다.
- 현재 첨부본은 확률표 학습까지이며, 테스트 예측 성능·모델 선택·최종 분석 결론은 아직 포함되어 있지 않다.

[Notion 원문](https://app.notion.com/p/403917c0e640809587cecf6923c366d0) · [분석 보고서](files/w11_bayesian_analysis_신정윤.pdf) · [노트북](files/w11_bayesian_analysis_신정윤.ipynb)

## 남은 확인 사항

- 박중현: 보고서에 대응하는 분석 노트북과 실행 환경을 추가로 확보한다.
- 강재성: 노트북이 읽는 `../data/raw/secom.data`, `secom_labels.data`는 이번 첨부에 없다. 재현 전에 데이터 준비와 실행 위치를 확인한다. 보고서의 ‘1차 조정’ 결과는 현재 노트북에 별도 실험 코드·출력으로 보존되어 있지 않다.
- 신정윤: 보고서의 K2 구조는 56개 간선이지만, 노트북 후반에서는 부모 수를 3개로 제한해 23개 간선으로 다시 학습한다. 최종 구조에 맞춰 보고서를 갱신하고 예측 평가와 결론을 보완한다.
- W11 회의록: 주차 페이지에는 TODO와 회의록 자리만 있으며, 실제 논의·결정 사항 본문은 확인되지 않았다.

노트북은 이번 정리에서 실행하지 않았으며, 저장된 코드와 출력만 확인했다. Notion의 ‘시작 전’ 표시와 달리 박중현·신정윤 페이지에도 실제 첨부가 있어, 위 표는 상태값이 아닌 파일 확인 결과를 따른다.

## 원본 파일명

| 스터디원 | Notion 첨부 이름 | 저장한 이름 |
| --- | --- | --- |
| 박중현 | `w11_bayesian_analysis_박중현.pdf` | 동일 |
| 강재성 | `반도체_공정_불량_분류_실습.pdf` | `w11_bayesian_analysis_강재성.pdf` |
| 강재성 | `03_secom_bayes.ipynb` | `w11_bayesian_analysis_강재성.ipynb` |
| 강재성 | `베이지안_분류기_수학_발표_EM.pdf` | `w11_bayesian_analysis_supplement_math_강재성.pdf` |
| 신정윤 | `w11_bayes_analysis.pdf` | `w11_bayesian_analysis_신정윤.pdf` |
| 신정윤 | `w4_bayes_credit_score.ipynb` | `w11_bayesian_analysis_신정윤.ipynb` |
