# PCA · W5 analysis

[Notion W5](https://app.notion.com/p/3c4917c0e64080ce828fc42dfd3a8aae)

| 작성자 | 분석 주제 | 보고서 | 노트북 | Notion 원본 |
|---|---|---|---|---|
| 박중현 | 문화시설 접근성과 종합문화취약지수 | [PDF · 2쪽](files/w5_pca_analysis_박중현.pdf) | [IPYNB](files/w5_pca_analysis_박중현.ipynb) | [개인 페이지](https://app.notion.com/p/a24917c0e64083f8b51b01cd4df92773) |
| 강재성 | SECOM 반도체 공정의 불량 분류 | [PDF · 7쪽](files/w5_pca_analysis_강재성.pdf) | [IPYNB](files/w5_pca_analysis_강재성.ipynb) | [개인 페이지](https://app.notion.com/p/3e0917c0e64080ee9635d9caafdcf7d3) |
| 신정윤 | AI 의존도 예측 | [PDF · 13쪽](files/w5_pca_analysis_신정윤_ai_dependency.pdf) | [IPYNB](files/w5_pca_analysis_신정윤_ai_dependency.ipynb) | [개인 페이지](https://app.notion.com/p/3c5917c0e6408023aaf3df067d9ec407) |
| 신정윤 | 유방암 예측 실습 | [PDF · 13쪽](files/w5_pca_analysis_신정윤_breast_cancer.pdf) | [IPYNB](files/w5_pca_analysis_신정윤_breast_cancer.ipynb) | [개인 페이지](https://app.notion.com/p/3c5917c0e6408023aaf3df067d9ec407) |

## 분석 요약

<!-- notion-assignment-sync:analysis:start -->
### 박중현 · 문화시설 접근성과 취약지수

- 서울 100m 격자의 문화시설 접근성을 선호 반영 H3SFCA와 선호 미반영 SFCA로 나누어 비교합니다.
- 기본 취약지표와 시설 중분류별 확장 지표에 PCA를 적용해 상관관계·설명분산·성분 로딩을 살펴봅니다.
- 보고서는 생활밀착형·목적지형 접근성이 서로 다른 축으로 나타나며, 취약성을 단일 축으로 요약하기 어렵다고 설명합니다.
- PCA를 정책 가중치의 대체값보다 하위지표 중복성과 공간적 취약성 구조를 해석하는 보조 분석으로 활용합니다.

### 강재성 · SECOM 불량 분류

- SECOM 반도체 공정 데이터의 결측치·상수 변수를 처리하고, Logistic Regression의 PCA 적용 전후를 비교합니다.
- 설명분산 비율에 따라 성분 수를 달리하며 차원축소와 분류 성능의 관계를 살펴봅니다.
- 단일 분할 실험에서는 450개 변수를 127개 성분으로 줄였을 때 불량 Recall이 높아지는 반면, Accuracy·F1·ROC-AUC는 낮아졌습니다.
- PCA의 효과를 전체 성능 향상으로 단정하지 않고, 불량 탐지 민감도·오경보·학습 효율 사이의 절충으로 해석합니다.

### 신정윤 · AI 의존도 및 유방암 예측 실습

- AI 의존도 실습은 합성 설문 응답의 이용·생활·심리 지표로 Logistic Regression·Random Forest·Gradient Boosting을 비교합니다.
- 원래 변수와 PCA 성분을 사용한 분류를 나란히 살펴보고, 예측력과 변수 해석의 차이를 정리합니다.
- 유방암 실습은 교육용 합성 데이터에 Logistic Regression·Decision Tree·Gradient Boosting을 적용한 PCA 전후 비교입니다.
- 두 보고서는 PCA 후 성능이 낮아지는 사례를 바탕으로, 분산 보존과 예측 성능이 같지 않다는 점을 논의합니다.

데이터: [AI 의존도 합성 응답 · CC0](https://www.kaggle.com/datasets/harpartapsingh13/ai-companion-dependency-prediction-dataset) · [유방암 교육용 합성 데이터](https://github.com/MobeenFatimaa/Breast-Cancer-Prediction-Dataset)
<!-- notion-assignment-sync:analysis:end -->
