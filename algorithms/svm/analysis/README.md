# SVM - Analysis

W8 SVM 미니 프로젝트 자료입니다. 주차 날짜는 2026-09-10입니다. [Notion W8](https://app.notion.com/p/3d7917c0e64080b488a1fb8fac6db852)

| 작성자 | 분석 주제 | 보고서 | 노트북 | Notion 본문 | 개인 과제 |
|---|---|---|---|---|---|
| 박중현 | 신용카드 사기 거래 이상 탐지 | [PDF](files/w8_svm_analysis_박중현.pdf) | [IPYNB](files/w8_svm_analysis_박중현.ipynb) | [본문](files/w8_svm_analysis_박중현.md) | [Notion](https://app.notion.com/p/92e917c0e64082a6b69d01e5a04a950a) |
| 강재성 | SECOM 반도체 공정 불량 분류 | [PDF](files/w8_svm_analysis_강재성.pdf) | [IPYNB](files/w8_svm_analysis_강재성.ipynb) | [본문](files/w8_svm_analysis_강재성.md) | [Notion](https://app.notion.com/p/3d7917c0e64080abb411efb37d8d8962) |
| 신정윤 | SNS 게시물 3종 감성 분류 | [PDF](files/w8_svm_analysis_신정윤.pdf) | [IPYNB](files/w8_svm_analysis_신정윤.ipynb) | [본문](files/w8_svm_analysis_신정윤.md) | [Notion](https://app.notion.com/p/3d7917c0e64080cbbaa2d56e5971b1e8) |

강재성 과제의 [프로젝트 묶음 ZIP](files/w8_svm_analysis_강재성_project.zip)도 원본 그대로 보존했습니다. 박중현 과제는 Notion 상태가 `시작 전`이지만 보고서와 노트북이 실제 첨부되어 있습니다. 강재성·신정윤 과제 상태는 `완료`입니다.

## 요약

<!-- notion-assignment-sync:analysis:start -->
### 박중현

- Credit Card Fraud Detection 데이터에서 중복을 제거한 283,726건을 시간 순서로 학습·검증·테스트에 나누어 사기 거래를 탐지한다.
- 정상 거래 중심의 One-Class SVM, Isolation Forest, Autoencoder를 비교하고 노트북에는 지도학습 Logistic Regression 기준선도 포함했다.
- 노트북의 테스트 PR-AUC는 OC-SVM 0.178556, Autoencoder 0.140527, Isolation Forest 0.031472이며, Logistic Regression은 0.737503이다.
- 보고서와 노트북의 실험 구성·수치가 달라 아래에 구분했다. 지도학습 기준선은 라벨과 학습 표본 조건도 다르므로 비지도 모델과 단순히 동등한 비교로 보지 않는다.

### 강재성

- SECOM 공정 데이터 1,567건의 불량 104건을 탐지하며 결측치 처리, 상수 변수 제거와 표준화를 거쳐 Linear/RBF SVM을 비교한다.
- 임계값 조정, PCA와 SelectKBest를 실험해 선택된 35개 변수에 RBF SVM을 적용했다.
- 최종 테스트 결과는 Balanced Accuracy 0.6408, 불량 Recall 0.4762, ROC-AUC 0.7754로, 불량 21건 중 10건을 탐지했다.
- 같은 테스트 세트를 여러 실험에서 확인한 한계가 있어 독립 홀드아웃이나 Nested Cross Validation을 통한 추가 검증이 필요하다.

### 신정윤

- SNS 게시물 732건을 부정·중립·긍정으로 묶고 텍스트와 플랫폼·국가·해시태그 등 메타데이터를 함께 사용한다.
- TF-IDF와 메타데이터 특성으로 Linear/RBF SVM을 학습하고 Logistic Regression, DistilBERT와 비교했다.
- 최종 비교에서 Linear SVM의 Accuracy는 0.857, Macro F1은 0.797로, Logistic Regression과 비슷하면서 Macro F1은 조금 높았다.
- 작은 표본과 중립 클래스 부족이 한계이며, 이 실험의 DistilBERT는 중립 Recall이 0이어서 클래스별 지표를 함께 확인해야 한다.
<!-- notion-assignment-sync:analysis:end -->

## 박중현 보고서·노트북 결과 구분

두 자료를 모두 보존합니다. 원래 보고서 파일명은 `w3_svm_anlaysis_박중현.pdf`이지만 W8 개인 과제의 첨부이므로 이 폴더에서는 W8로 정리했습니다. Notion의 첨부 표시명에 있던 `구버전`만으로 결과물을 제외하거나 최종 여부를 단정하지 않았습니다.

| 테스트 PR-AUC | 보고서 PDF | 노트북 저장 결과 |
|---|---:|---:|
| 정상 거래 학습 OC-SVM | 0.076431 | 0.178556 |
| 정상 거래 학습 Autoencoder | 0.128372 | 0.140527 |
| 정상 거래 학습 Isolation Forest | 0.031472 | 0.031472 |
| 지도학습 Logistic Regression | 비교 대상에 없음 | 0.737503 |

보고서에는 정상·사기 혼합 데이터로 학습한 추가 모델 실험도 있습니다. 따라서 두 문서를 동일한 실험의 일치하는 결과로 볼 수 없으며, 발표용 최종 결과를 하나로 정할 때는 보고서와 노트북을 같은 실험 설정으로 맞춰야 합니다. 위 수치는 첨부에 저장된 결과이며 이번 동기화에서 코드를 재실행하지 않았습니다.

회의 기록은 [W8 기록](../../../meetings/w8_svm_analysis.md)을 참고하세요. Notion에는 W7과 동일한 후속 학습 체크리스트가 반복되어 있습니다.
