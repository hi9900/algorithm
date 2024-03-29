# 다이나믹 프로그래밍

## 효율적인 화폐 구성

N가지 종류의 화폐를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려 한다.

이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

입력 조건

- 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)

- 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건

- 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.

- 불가능할 때는 `-1`을 출력한다.

```
입력 예시 1
2 15
2
3
```

```
출력 예시 1
5
```

```
입력 예시 2
3 4
3
5
7
```

```
출력 예시 2
-1
```

---

### [문제 풀이](./7-4.py)

### 문제 해설

그리디에서 다루었던 거스름돈 문제와 거의 동일하다. 단 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점만 다르다. 따라서 그리디 알고리즘처럼 가장 큰 화폐 단위부터 처리하는 방법으로는 해결할 수 없다.

이 문제는 다이나믹 프로그래밍 방식으로 해결해야 한다. 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾으면 된다.

금액 i를 만들 수 있는 최소한의 화폐 개수를 k라고 할 때, 점화식은 다음과 같다. `f(i-k)`는 `(i-k)`를 만들 수 있는 최소한의 화폐 개수를 의미한다.

- `f(i-k)`를 만드는 방법이 존재하는 경우, `f(i) = min(f(i), f(i-k) + 1)`

- `f(i-k)`를 만드는 방법이 존재하지 않는 경우, `f(i) = 10,001`

위의 점화식을 모든 화폐 단위에 대해 차례대로 적용한다.

K의 크기만큼 리스트를 할당한다. 각 인덱스는 "금액"으로 고려하여 메모이제이션을 진행한다.
