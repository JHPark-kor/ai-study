# w7_svm_PapaerReview

상태: 완료
담당자: JAESUNGKANG
파일: [SVM 논문리딩 Wafer Classification 보고서](w7_wafer_classification_jaesung.pdf)

[SVM_논문리딩_Wafer_Classification_보고서 (2).pdf](w7_wafer_classification_jaesung.pdf)

# 7주차 — SVM 실제 반도체 활용 논문 리딩

### 학습 주제

SVM 활용 사례 논문 조사

### 선정 논문

**Baly, R. & Hajj, H. (2012)**

*Wafer Classification Using Support Vector Machines*

IEEE Transactions on Semiconductor Manufacturing

### 연구 문제

반도체 웨이퍼의 최종 EOL 검사까지 기다리지 않고, 공정 중간에서 얻은 측정 데이터만을 이용해 **Low-Yield / High-Yield 웨이퍼를 조기에 분류할 수 있는가?**

### 데이터

실제 IC 제조시설 데이터 2개 사용

**Dataset 1**

- 1,150 wafers
- 138 variables

**Dataset 2**

- 238 wafers
- 30 variables

### 적용 방법

- Z-score normalization
- Gaussian RBF Kernel SVM
- Yield Threshold 설정
- Kernel width (\sigma) 선택
- Penalty (C) 선택
- Cross Validation을 이용한 파라미터 탐색

### 비교 모델

- C4.5 Decision Tree
- kNN
- PLS Regression
- GRNN

### 평가 지표

- Classification Accuracy
- False Negative

특히 실제 Bad Wafer를 Good Wafer라고 판단하는 False Negative를 제조 관점에서 중요한 위험으로 평가했다.

### 주요 결과

- SVM은 다른 분류기와 같거나 더 높은 Accuracy를 보임
- False Negative가 비교 모델 중 낮게 나타남
- Dataset 1에서 138개 변수 중 40개만 사용해도 성능이 유지 또는 개선됨
- 공정 변화 이후 Adaptive Model Update를 적용하면 성능이 개선됨

### 논문의 의미

이 논문의 핵심은 단순히 SVM의 정확도가 높다는 것이 아니라,

**비선형·다변량 공정 데이터에 RBF-SVM을 적용하고 → 파라미터를 검증하고 → 공정 변화에 따라 모델까지 갱신**

하는 방식으로 머신러닝을 실제 제조 운영 흐름에 연결했다는 점이다.

### 한계

- 기업 데이터라 원본 데이터 공개 X
- 정확한 Yield 값 비공개
- 논문 결과의 완전한 재현이 어려움
- Threshold 위치에 따라 분류 성능이 달라질 수 있음
