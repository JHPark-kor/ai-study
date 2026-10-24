# SVM - Analysis

W8 SVM 데이터 분석 미니 프로젝트 자료입니다. 2026-09-10 · [Notion W8](https://app.notion.com/p/3d7917c0e64080b488a1fb8fac6db852)

| 작성자 | 분석 주제 | 보고서 | 노트북 | Notion 본문 | 개인 과제 |
|---|---|---|---|---|---|
| 박중현 | 신용카드 사기 거래 이상 탐지 | [PDF](files/w8_svm_analysis_박중현.pdf) | [IPYNB](files/w8_svm_analysis_박중현.ipynb) | [본문](files/w8_svm_analysis_박중현.md) | [Notion](https://app.notion.com/p/92e917c0e64082a6b69d01e5a04a950a) |
| 강재성 | SECOM 반도체 공정 불량 분류 | [PDF](files/w8_svm_analysis_강재성.pdf) | [IPYNB](files/w8_svm_analysis_강재성.ipynb) | [본문](files/w8_svm_analysis_강재성.md) | [Notion](https://app.notion.com/p/3d7917c0e64080abb411efb37d8d8962) |
| 신정윤 | SNS 게시물 3종 감성 분류 | [PDF](files/w8_svm_analysis_신정윤.pdf) | [IPYNB](files/w8_svm_analysis_신정윤.ipynb) | [본문](files/w8_svm_analysis_신정윤.md) | [Notion](https://app.notion.com/p/3d7917c0e64080cbbaa2d56e5971b1e8) |

강재성 · [SECOM 프로젝트 파일](files/w8_svm_analysis_강재성_project.zip)

## 요약

<!-- notion-assignment-sync:analysis:start -->
### 박중현

- Credit Card Fraud Detection 데이터에서 중복을 제거하고 시간 순서로 학습·검증·테스트를 나누어 사기 거래를 탐지했다.
- 정상 거래 중심의 One-Class SVM, Isolation Forest, Autoencoder를 비교하고 Logistic Regression을 지도학습 기준선으로 살펴봤다.
- PR-AUC를 중심으로 희소한 사기 거래의 탐지 성능을 비교하며, 정상 데이터만으로 학습하는 이상 탐지의 가능성을 살펴봤다.
- 지도학습 기준선과 비지도 모델은 사용하는 라벨과 학습 표본 조건이 달라, 성능을 각 학습 조건 안에서 해석했다.

### 강재성

- SECOM 공정 데이터 1,567건의 불량 104건을 탐지하며 결측치 처리, 상수 변수 제거와 표준화를 거쳐 Linear/RBF SVM을 비교한다.
- 임계값 조정, PCA와 SelectKBest를 실험해 선택된 35개 변수에 RBF SVM을 적용했다.
- 선택한 모델의 테스트 결과는 Balanced Accuracy 0.6408, 불량 Recall 0.4762, ROC-AUC 0.7754로, 불량 21건 중 10건을 탐지했다.
- 높은 정확도만으로 불량 탐지를 평가하기 어렵다는 점과, 여러 실험에서 같은 테스트 세트를 사용한 해석상의 한계를 함께 다뤘다.

### 신정윤

- SNS 게시물 732건을 부정·중립·긍정으로 묶고 텍스트와 플랫폼·국가·해시태그 등 메타데이터를 함께 사용한다.
- TF-IDF와 메타데이터 특성으로 Linear/RBF SVM을 학습하고 Logistic Regression, DistilBERT와 비교했다.
- 비교 실험에서 Linear SVM의 Accuracy는 0.857, Macro F1은 0.797로, Logistic Regression과 비슷하면서 Macro F1은 조금 높았다.
- 작은 표본과 중립 클래스 부족을 분석의 한계로 정리했으며, DistilBERT의 중립 Recall이 0으로 나타나 클래스별 성능 차이를 살펴봤다.
<!-- notion-assignment-sync:analysis:end -->

[W8 학습 기록](../../../meetings/w8_svm_analysis.md)
