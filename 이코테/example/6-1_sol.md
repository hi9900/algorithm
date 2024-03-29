# 이진 탐색

## 부품 찾기

전자 매장에 부품 N개가 있다. 각 부품은 정수 형태의 고유한 번호를 가진다.

손님이 M개 종류의 부품 구매할 때 매장에 부품이 모두 있는 지 확인하라.

입력 조건

- 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)

- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

- 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)

- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

출력 조건

- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력한다.

```
입력 예시
5
8 3 7 9 2
3
5 7 9
```

```
출력 예시
no yes yes
```

---

### [문제 풀이](./6-1.py)

### 문제 해설

다량의 데이터 검색은 이진 탐색 알고리즘을 이용해 효과적으로 처리할 수 있다.

1. 매장 내 N개의 부품을 번호를 기준으로 정렬한다.

2. M개의 찾고자 하는 부품이 각각 존재하는 지 검사한다.

부품을 찾는 과정에서 최악의 경우 시간 복잡도 `O(M X logN)`, 이론상 최대 약 200만번의 연산

N개의 부품을 정렬하기 위해 요구되는 시간 복잡도는 `O(N X logN)`, 이론상 최대 약 2,000만번의 연산

결과적으로 문제 풀이의 시간복잡도는 `O((M+N) X logN)`

---

계수 정렬을 이용해 문제를 풀 수 있다.

1. 모든 원소의 번호를 포함하는 크기의 리스트를 생성한다.

2. 리스트의 인덱스에 접근하여 특정 번호의 부품이 존재하는 지 확인한다.

---

단순히 특정한 수가 한 번이라도 등장했는 지 검사하면 되므로 집합 자료형을 이용해 문제를 해결할 수 있다.

1. 가게에 있는 전체 부품 번호를 집합(set) 자료형으로 기록한다.

2. 요청한 부품 번호를 하나씩 확인하며 존재하는 지 확인한다.
