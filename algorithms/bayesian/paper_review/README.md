# Bayesian · W10 paper_review

W10에서는 나이브 베이즈와 베이지안 네트워크가 텍스트, 제조, 임상 데이터에서 활용되는 사례를 읽었습니다.

| 작성자 | 논문·리뷰 주제 | 자료 | Notion |
|---|---|---|---|
| 박중현 | 나이브 베이즈 기반 소셜 미디어 상의 신조어 감성 판별 기법 | [리뷰 PDF](files/w10_bayesian_paper_review_박중현.pdf) | [개인 과제](https://app.notion.com/p/430917c0e64083c28af8814e2d896bf5) |
| 강재성 | Cycle-Time Key Factor Identification and Prediction in Semiconductor Manufacturing Using Machine Learning and Data Mining | [리뷰 PDF](files/w10_bayesian_paper_review_강재성.pdf) | [개인 과제](https://app.notion.com/p/3e0917c0e64080cabfe8f4664caf41ef) |
| 신정윤 | 베이지안 네트워크를 이용한 임상 데이터의 결측 정보 활용 | [리뷰 PDF](files/w10_bayesian_paper_review_신정윤.pdf) | [개인 과제](https://app.notion.com/p/3e9917c0e64080eb8e32cf4dbcea0b51) |

## 박중현

- 신조어의 의미가 기존 사전에 충분히 담기지 않아 감성 분석에서 놓치는 정보를 살펴봤습니다.
- 신조어와 일반어를 각각 학습한 나이브 베이즈 분류를 결합하고, 형태소 분석·불용어 제거·TF-IDF 등의 처리 흐름을 정리했습니다.
- 신조어를 함께 반영하면 일반어 중심 모델보다 감성 강도의 차이를 더 민감하게 포착하는 사례를 확인했습니다.
- 이 차이를 객관적인 분류 정확도 향상으로 단정하기보다, 감성 표현을 더 풍부하게 반영한 결과로 해석했습니다.

## 강재성

- 반도체 제조의 Cycle Time과 관련된 핵심 공정 요인을 찾는 연구를 정리했습니다.
- CMIM으로 후보 변수를 압축한 뒤 Selective Naive Bayes를 적용해 182개 후보 요인을 약 20개로 줄였습니다.
- 리뷰에 제시된 대표 설정의 평균 정확도는 72.6%이며, 적은 변수로 예측과 해석을 함께 수행한다는 점에 주목했습니다.
- 모의 Fab 데이터의 결과라는 점과 실제 공정 변수 간 의존성 때문에 조건부 독립 가정이 완전히 성립하기 어렵다는 한계도 살펴봤습니다.

## 신정윤

- 임상 데이터에서 검사가 시행되지 않았다는 사실 등 결측 자체가 예측 정보를 가질 수 있는지 살펴봤습니다.
- 결측을 그대로 두거나 대체하는 방식과, 별도의 상태·지시 변수로 명시하는 방식을 여러 베이지안 네트워크 구조에서 비교했습니다.
- AUC와 500회 부트스트랩, 순열검정을 통해 결측 정보를 명시한 방식이 전반적으로 더 좋은 성능을 보였다는 결과를 정리했습니다.
- 목표는 병명을 확정하는 자동 진단이 아니라 문제 목록을 보완하는 의사결정지원이며, 다중질환과 실제 임상 적용에는 추가 검토가 필요합니다.

[W10 Notion 페이지](https://app.notion.com/p/3e0917c0e64080f0be89f9b1d651bee6) · [회의록](../../../meetings/w10_bayesian_paper_review.md)
