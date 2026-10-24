# AI/ML 스터디

저희 AI/ML 스터디 팀은 **다양한 알고리즘 기법과 이를 활용한 데이터 분석 기반의 문제 해결**에 관심 있는 3인으로 이루어져 있습니다.

1. **알고리즘 학습**<br />
   알고리즘의 수학적 원리와 구현 방식을 학습합니다.

2. **분석 논문·사례 리뷰**<br />
   해당 알고리즘을 사용한 논문과 분석 사례를 함께 읽고, 어떤 산업 분야에서 어떤 상황에 쓰일 수 있을지 고민합니다. 알고리즘의 장단점과 성능, 한계점에 대해 함께 토의합니다.

3. **데이터 분석 미니 프로젝트**<br />
   학습한 알고리즘을 직접 데이터 분석에 활용합니다. **문제 정의 - 분석 기획 - EDA 및 분석 - 결과와 인사이트 도출 - 분석 보고서 작성** 후 각자 수행했던 프로젝트를 발표합니다.

<br />

<!-- 사용자 제공 과제 사진을 유형별 두 장씩 배치한다. 별도 Study Flow 섹션은 두지 않는다. -->

<table>
  <thead>
    <tr>
      <th width="220">1주차<br />알고리즘 학습</th>
      <th width="24">→</th>
      <th width="220">2주차<br />논문·사례 페이퍼 리뷰</th>
      <th width="24">→</th>
      <th width="220">3주차<br />데이터 분석 미니 프로젝트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" valign="top"><a href="assets/readme/examples/math-likelihood.png"><img src="assets/readme/examples/math-likelihood.png" width="200" alt="베이지안 분류기의 최대우도추정: 우도와 로그우도" /></a><br /><br /><strong>베이지안 분류기의<br />우도와 로그우도</strong></td>
      <td rowspan="2"></td>
      <td align="center" valign="top"><a href="assets/readme/examples/paper-sentiment.png"><img src="assets/readme/examples/paper-sentiment.png" width="200" alt="Naive Bayes 기반 신조어 감성분석 논문 사례" /></a><br /><br /><strong>Naive Bayes 기반<br />감성분석 논문 사례 정리</strong></td>
      <td rowspan="2"></td>
      <td align="center" valign="top"><a href="assets/readme/examples/analysis-bayesian.png"><img src="assets/readme/examples/analysis-bayesian.png" width="200" alt="Bayesian Network를 적용한 문화예술 관람 의향 분석 보고서" /></a><br /><br /><strong>Bayesian Network 적용<br />미니 프로젝트 보고서</strong></td>
    </tr>
    <tr>
      <td align="center" valign="top"><a href="assets/readme/examples/math-kernel.png"><img src="assets/readme/examples/math-kernel.png" width="200" alt="SVM 커널 함수와 고차원 특징 공간" /></a><br /><br /><strong>SVM 커널 함수</strong></td>
      <td align="center" valign="top"><a href="assets/readme/examples/paper-pca.png"><img src="assets/readme/examples/paper-pca.png" width="200" alt="PCA 논문의 주성분 개수 선정 기준과 적용 결과" /></a><br /><br /><strong>PCA 주성분 논문 요약</strong></td>
      <td align="center" valign="top"><a href="assets/readme/examples/analysis-eda.png"><img src="assets/readme/examples/analysis-eda.png" width="200" alt="SVM 미니 프로젝트의 학습 데이터 EDA 코드와 시각화 결과" /></a><br /><br /><strong>SVM 미니 프로젝트 코드</strong></td>
    </tr>
  </tbody>
</table>

<br />

### 사용 툴

<table>
  <tbody>
    <tr>
      <td width="240" align="center"><img src="assets/readme/tools/python.svg" width="48" height="48" alt="Python" /><br /><strong>Python</strong><br />데이터 EDA · 분석 · 모델링<br />시각화 · 통계 분석</td>
      <td width="240" align="center"><img src="assets/readme/tools/postgresql.svg" width="48" height="48" alt="PostgreSQL" /><br /><strong>PostgreSQL</strong><br />데이터 ETL · 조회 · 분석</td>
      <td width="240" align="center"><img src="assets/readme/tools/notion.svg" width="48" height="48" alt="Notion" /><br /><strong>Notion</strong><br />일정 관리 · 협업<br />산출물 기록 · 보고서 작성</td>
    </tr>
  </tbody>
</table>

<br />

### 참여 팀원

| 팀원 | GitHub |
|---|---|
| 박중현 | [JHPark-kor](https://github.com/JHPark-kor) |
| 강재성 | [jaesung0306](https://github.com/jaesung0306) |
| 신정윤 | [wjddbsl03](https://github.com/wjddbsl03) |

<br /><br />

## 스터디 기록

아래 링크를 클릭하시면 필기노트, 페이퍼 리뷰 보고서, 미니 프로젝트 분석 보고서와 관련 코드를 보실 수 있습니다.

<!-- 동일 알고리즘은 rowspan으로 묶는다. 주차를 추가할 때 해당 rowspan도 함께 갱신한다. -->
<!-- 제출 여부는 원본 파일을 확인한 주차만 갱신한다. -->

<table>
  <thead>
    <tr>
      <th>주차</th>
      <th>알고리즘</th>
      <th>내용</th>
      <th>상세 내용</th>
      <th>회의록</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>W3</td>
      <td rowspan="3"><a href="algorithms/pca/README.md">PCA</a></td>
      <td><strong>수학 원리 학습</strong><br />분산 최대화 · 고유값 분해 · 커널 PCA</td>
      <td><a href="algorithms/pca/math_theory/README.md">PCA 수학 원리</a></td>
      <td>—</td>
    </tr>
    <tr>
      <td>W4</td>
      <td><strong>논문·사례 리뷰</strong><br />PCA 기반 복합지표 · 공정 이상 탐지<br />기상 재해 피해 추정</td>
      <td><a href="algorithms/pca/paper_review/README.md">PCA 논문 리뷰</a></td>
      <td>—</td>
    </tr>
    <tr>
      <td>W5</td>
      <td><strong>데이터 분석 미니 프로젝트</strong><br />문화 접근성 · 반도체 불량 분류<br />AI 의존도 예측</td>
      <td><a href="algorithms/pca/analysis/README.md">PCA 미니 프로젝트</a></td>
      <td>—</td>
    </tr>
    <tr>
      <td>W6</td>
      <td rowspan="3"><a href="algorithms/svm/README.md">SVM</a></td>
      <td><strong>수학 원리 학습</strong><br />마진 최대화 · KKT 조건 · 커널 함수</td>
      <td><a href="algorithms/svm/math_theory/README.md">SVM 수학 원리</a></td>
      <td>—</td>
    </tr>
    <tr>
      <td>W7</td>
      <td><strong>논문·사례 리뷰</strong><br />One-Class SVM 낙상 탐지<br />웨이퍼 분류 · SVM 영화 리뷰 감성분석</td>
      <td><a href="algorithms/svm/paper_review/README.md">SVM 논문 리뷰</a></td>
      <td><a href="meetings/w7_svm_paper_review.md">후속 학습 기록</a></td>
    </tr>
    <tr>
      <td>W8</td>
      <td><strong>데이터 분석 미니 프로젝트</strong><br />사기 거래 탐지 · 반도체 불량 분류<br />SNS 감성분석</td>
      <td><a href="algorithms/svm/analysis/README.md">SVM 미니 프로젝트</a></td>
      <td><a href="meetings/w8_svm_analysis.md">기록 확인</a></td>
    </tr>
    <tr>
      <td>W9</td>
      <td rowspan="3"><a href="algorithms/bayesian/README.md">Bayesian</a></td>
      <td><strong>수학 원리 학습</strong><br />최대우도·로그우도 · 나이브 베이즈<br />베이지안 네트워크</td>
      <td><a href="algorithms/bayesian/math_theory/README.md">Bayesian 수학 원리</a></td>
      <td>—</td>
    </tr>
    <tr>
      <td>W10</td>
      <td><strong>논문·사례 리뷰</strong><br />Naive Bayes 신조어 감성분석<br />제조 Cycle Time · 임상 결측 정보 활용</td>
      <td><a href="algorithms/bayesian/paper_review/README.md">Bayesian 논문 리뷰</a></td>
      <td><a href="meetings/w10_bayesian_paper_review.md">회의록</a></td>
    </tr>
    <tr>
      <td>W11</td>
      <td><strong>데이터 분석 미니 프로젝트</strong><br />문화예술 관람 의향 · 반도체 불량 분류<br />신용카드 연체 구조 설계</td>
      <td><a href="algorithms/bayesian/analysis/README.md">Bayesian 미니 프로젝트</a></td>
      <td><a href="meetings/w11_bayesian_analysis.md">회의록</a></td>
    </tr>
    <tr>
      <td>W12</td>
      <td>선형회귀</td>
      <td><strong>수학 원리 토의</strong><br />최소제곱법 · 로지스틱 회귀 · 볼록함수</td>
      <td><a href="https://app.notion.com/p/3ef917c0e6408077907be85f4461eb26">선형회귀 수학 원리</a></td>
      <td><a href="meetings/w12_linear_math_theory.md">회의록</a></td>
    </tr>
  </tbody>
</table>

<br /><br />

## Side Projects (사이드 프로젝트)

### 01. 데이터 EDA 자동화 플랫폼 만들기 (AI agent 기반)

<!-- 개요는 과제발굴정의서를 확인한 뒤 작성한다. 목표를 이미 달성한 성과처럼 기재하지 않는다. -->

#### 개요

| 항목 | 내용 |
|---|---|
| 문제 정의 | 〈과제발굴정의서 기반 내용〉 |
| 목표 | 〈과제발굴정의서 기반 내용〉 |
| 기대효과 | 〈과제발굴정의서 기반 내용〉 |

#### 사용 사례

| 실행 방법 | 주요 결과 페이지 | 산출물 결과 |
|---|---|---|
| 〈실제 실행 화면 이미지〉 | 〈실제 결과 화면 이미지〉 | 〈실제 산출물 이미지〉 |
| 〈사진 아래 설명〉 | 〈사진 아래 설명〉 | 〈사진 아래 설명〉 |

#### 관련 자료

| 자료 | 링크 |
|---|---|
| 과제발굴정의서 | 〈문서 링크〉 |
| 배포 코드 | 〈프로젝트 저장소 링크〉 |

<!-- 배포 코드의 실행 방법과 코드별 설명서는 연결할 프로젝트 저장소의 메인 README에 둔다. -->
