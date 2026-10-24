# PCA · W5 analysis

[Notion 주차 페이지](https://app.notion.com/p/3c4917c0e64080ce828fc42dfd3a8aae)의 보고서 PDF 4개와 노트북 4개를 확인했습니다. 원본 파일은 수정하지 않았으며, 요약은 보고서와 노트북의 저장된 내용에 근거합니다. 이번 정리 과정에서 노트북을 실행하지는 않았습니다.

| 작성자 | 분석 주제 | 보고서 | 노트북 | Notion 원본 |
|---|---|---|---|---|
| 박중현 | 문화시설 접근성과 종합문화취약지수 | [PDF · 2쪽](files/w5_pca_analysis_박중현.pdf) | [IPYNB](files/w5_pca_analysis_박중현.ipynb) | [개인 페이지](https://app.notion.com/p/a24917c0e64083f8b51b01cd4df92773) |
| 강재성 | SECOM 반도체 공정의 불량 분류 | [PDF · 7쪽](files/w5_pca_analysis_강재성.pdf) | [IPYNB](files/w5_pca_analysis_강재성.ipynb) | [개인 페이지](https://app.notion.com/p/3e0917c0e64080ee9635d9caafdcf7d3) |
| 신정윤 | AI 의존도 예측 | [PDF · 13쪽](files/w5_pca_analysis_신정윤_ai_dependency.pdf) | [IPYNB](files/w5_pca_analysis_신정윤_ai_dependency.ipynb) | [개인 페이지](https://app.notion.com/p/3c5917c0e6408023aaf3df067d9ec407) |
| 신정윤 | 유방암 예측 실습 | [PDF · 13쪽](files/w5_pca_analysis_신정윤_breast_cancer.pdf) | [IPYNB](files/w5_pca_analysis_신정윤_breast_cancer.ipynb) | [개인 페이지](https://app.notion.com/p/3c5917c0e6408023aaf3df067d9ec407) |

## 분석 요약

<!-- notion-assignment-sync:analysis:start -->
### 박중현 · 문화시설 접근성과 취약지수

- 서울 100m 격자를 대상으로 선호 반영 H3SFCA와 선호 미반영 SFCA의 문화시설 접근성 구조를 비교했습니다.
- 기본 취약지표 4개와 시설 중분류를 나눈 확장 지표 13개에 PCA를 적용하는 코드를 정리했습니다.
- 보고서에서는 확장 지표의 PC1 설명력이 약 21%여서 단일 축으로 요약하기 어렵고, 생활밀착형·목적지형 접근성이 서로 다른 축으로 나타났다고 설명합니다.
- 최종 정책 지수에는 기존 가중합을 유지하고, PCA는 하위지표 중복성과 공간적 취약성 구조를 설명하는 보조 분석으로 활용했습니다.

### 강재성 · SECOM 불량 분류

- SECOM의 590개 센서 변수를 학습 데이터 기준으로 전처리해 450개로 줄이고, Logistic Regression의 PCA 적용 전후를 비교했습니다.
- 저장된 단일 분할 결과에서 설명분산 90% 기준 PCA는 127개 성분을 사용했고, Fail Recall은 0.1905에서 0.2381로 높아졌습니다.
- Balanced Accuracy는 0.5389에서 0.5337로 소폭 낮아졌으며 Accuracy·F1·ROC-AUC도 감소해, 차원축소와 탐지 민감도의 절충으로 해석했습니다.
- 보고서에는 5-fold 교차검증 결과도 있지만, 제출 노트북에서 해당 계산과 저장 결과는 확인되지 않아 별도 검증 자료가 필요합니다.

### 신정윤 · AI 의존도 예측

- 1,000명의 설문 응답을 모사한 합성 데이터의 AI 이용·생활·심리 지표에서 식별자와 일일 채팅시간을 제외하고 AI 의존도 세 범주를 예측했습니다.
- 저장 결과에서는 47개 입력 변수를 PCA 30개 성분으로 줄인 뒤 Logistic Regression·Random Forest·Gradient Boosting을 비교했습니다.
- Random Forest 정확도는 0.775에서 0.750으로 낮아졌고, 세 모델 모두 PCA 후 성능이 떨어져 원래 변수의 해석과 예측력을 유지하는 방향을 제안했습니다.
- 다만 전체 데이터에 표준화·PCA를 먼저 적용한 뒤 분할한 코드이므로, 학습 데이터에만 전처리를 적합시킨 재검증 전까지 성능을 확정적으로 해석하기는 어렵습니다.

### 신정윤 · 유방암 예측 실습

- 교육용 합성 데이터 10,000행에서 식별자와 목표값을 직접 드러내는 변수를 제외하고 분류모형 세 가지를 비교했습니다.
- 보고서는 결측 처리 후 21개 변수를 16개 주성분으로 줄였을 때 세 모델의 정확도·F1이 모두 낮아졌다고 정리합니다.
- 원래 변수 기반 Gradient Boosting의 보고서 정확도는 0.997이지만, 이는 합성 데이터 실습 결과이며 실제 임상 성능으로 해석할 수 없습니다.
- 제출 노트북에는 모델링 코드가 있으나 해당 셀의 실행 결과가 저장되어 있지 않아, 보고서 수치를 노트북 출력으로 대조하는 데 한계가 있습니다.
<!-- notion-assignment-sync:analysis:end -->

## 추가 확인 사항

| 작성자 | 확인할 내용 |
|---|---|
| 박중현 | 기존 복원 노트북과 Notion 첨부의 SHA-256이 같아 기존 파일을 유지했습니다. 코드 셀 14개의 실행 횟수·출력이 모두 비어 있고, 입력 CSV 4개도 이번 첨부에 없어 보고서 수치의 재현에는 실행 결과와 데이터 준비 방법이 필요합니다. |
| 강재성 | 보고서의 5-fold CV 구현·결과가 제출 노트북에 없습니다. 28번 셀이 뒤의 33번 셀에서 만드는 `pca_results_df`를 먼저 참조하므로 위에서부터 재실행하기 전에 셀 순서 정리도 필요합니다. SECOM 입력 파일은 별도로 준비해야 합니다. |
| 신정윤 · AI 의존도 | 19번 셀의 분할 전 표준화·PCA와 CV 전처리 범위를 확인해야 합니다. PDF의 일부 소제목은 Decision Tree지만 실제 코드·결과표는 Random Forest이며, 일부 인코딩 설명도 코드와 다릅니다. |
| 신정윤 · 유방암 | PDF 9쪽 본문은 설명분산 90%, 그래프·코드는 95%로 표기가 다릅니다. 노트북의 모델링·PCA 결과를 저장하고 CV의 전처리·PCA를 각 fold 안에서 적합시키는지 확인해야 합니다. |

노트북의 저장된 오류 출력은 4개 모두 없지만, 이것이 재실행 성공을 의미하지는 않습니다. Notion의 `시작 전` 상태와 관계없이 박중현의 실제 보고서·노트북 첨부를 기준으로 기록했습니다. 신정윤 노트북의 원래 파일명은 `w2_pca_*.ipynb`였으며, W5 제출 페이지를 근거로 이름만 통일했습니다.

## 데이터 출처

- 강재성: 보고서에 UCI SECOM을 명시하고 노트북은 `secom.data`와 `secom_labels.data`를 읽습니다. 원시 데이터는 이번 첨부에 포함되지 않았습니다.
- 신정윤 · AI 의존도: 코드의 다운로드 대상인 [Kaggle AI Companion Dependency Prediction Dataset](https://www.kaggle.com/datasets/harpartapsingh13/ai-companion-dependency-prediction-dataset)의 원저자 Data Card는 1,000명의 설문 응답을 모사한 합성 데이터(1,000행·30열)이며 CC0 Public Domain이라고 명시합니다. 예시 행의 `user_id`는 실제 설문 참여자 신원으로 해석하지 않습니다.
- 신정윤 · 유방암: 코드의 [Kaggle 데이터](https://www.kaggle.com/datasets/mobeenfatimah/breast-cancer-prediction-dataset-10000-patient)와 연결된 [제작자 저장소](https://github.com/MobeenFatimaa/Breast-Cancer-Prediction-Dataset)는 실제 환자 정보가 없는 교육용 합성 데이터라고 명시합니다. 따라서 예시 행의 `Patient_ID`는 실제 환자 신원으로 해석하지 않습니다.
