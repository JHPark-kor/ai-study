# SVM - Paper Review

W7 SVM 논문 리뷰 자료입니다. 2026-08-29 · [Notion W7](https://app.notion.com/p/3c4917c0e64080b899c8e469becb91a1)

| 작성자 | 논문 | 개인 리뷰 PDF | Notion 본문 | 개인 과제 |
|---|---|---|---|---|
| 박중현 | 유지현·고진환(2025), 「초음파 어레이를 활용한 One-Class SVM 낙상 탐지」 | [리뷰](files/w7_svm_paper_review_박중현.pdf) | [본문·이미지](files/w7_svm_paper_review_박중현.md) | [Notion](https://app.notion.com/p/3ca917c0e640803181a8fb2ca4c71de6) |
| 강재성 | Baly, R. & Hajj, H. (2012), *Wafer Classification Using Support Vector Machines* | [리뷰](files/w7_wafer_classification_jaesung.pdf) | [본문](files/w7_svm_paper_review_강재성.md) | [Notion](https://app.notion.com/p/3cb917c0e64080c39945d7e1ed7cb300) |
| 신정윤 | *Sentiment Analysis for IMDb Movie Review Using SVM Method* | [리뷰](files/w7_svm_paper_review_신정윤.pdf) · [논문 원문](files/w7_imdb_sentiment_svm_wjddbsl03.pdf) | [본문](files/w7_svm_paper_review_신정윤.md) | [Notion](https://app.notion.com/p/3ca917c0e6408039896cc410effdb6e4) |

## 요약

### 박중현

- 낙상 탐지에서 이상 데이터 수집이 어렵다는 문제를 정상 데이터만 학습하는 One-Class SVM으로 다룬다.
- 초음파 어레이 신호를 이미지로 변환하고 TC-CNN, OC-CNN, OC-SVM을 비교했다.
- RBF 기반 OC-SVM은 정상 데이터만으로 높은 탐지 성능을 보여, 이상 사례가 부족한 상황에서의 활용 가능성을 살펴봤다.
- 모델별 학습 데이터 구성이 달라 성능 차이는 학습 조건과 함께 해석했다.

### 강재성

- 반도체 중간 공정 데이터로 웨이퍼를 Low-Yield / High-Yield로 조기 분류하는 연구다.
- 실제 IC 제조 데이터에 RBF SVM을 적용하고 교차검증으로 파라미터를 선택했다.
- 불량을 정상으로 판단하는 False Negative를 줄이는 것이 중요하며, 변수 선택과 공정 변화에 따른 모델 갱신도 살펴본다.
- 웨이퍼의 공정 변수와 품질 분류를 연결하는 접근을 SECOM 후속 실험의 문제 설정에 활용했다.

### 신정윤

- IMDb 영화 리뷰 50,000건을 긍정·부정으로 분류하는 SVM 기반 감성 분석 연구다.
- 텍스트 전처리 후 BoW와 TF-IDF로 벡터화하고 Grid Search로 SVM 파라미터를 탐색했다.
- 리뷰에서는 TF-IDF 기반 SVM이 BoW보다 높은 성능을 보였다고 정리하며, 특성 표현 방식의 중요성을 설명한다.
- 단어 순서와 문맥을 충분히 반영하지 못하는 한계, 정확도 외 지표와 오분류 분석의 필요성도 짚는다.

[W7 후속 학습 기록](../../../meetings/w7_svm_paper_review.md)
