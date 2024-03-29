# 모험가 길드

모험가 길드에서는 N명의 모험가를 대상으로 "공포도"를 측정했다. "공포도"가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.

모험가 길드장은 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다.

N명의 모험가에 대한 정보가 주어질 때, 여행을 떠날 수 있는 그룹의 최댓값을 구하라. 몇 명의 모험가는 마을에 그대로 남아있어도 되며, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.

입력 조건

- 첫째 줄에 모험가의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

- 둘째 줄에 각 모험가의 공포도의 값이 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다.

출력 조건

- 여행을 떠날 수 있는 그룹 수의 최댓값을 출력한다.

```
입력 예시
5
2 3 1 2 2
```

```
출력 예시
2
```

---

### 문제 접근

공포도가 낮은 모험가부터 그룹을 결성해 나간다.

1. 모험가 배열을 공포도 순으로 정렬한다.

2. 모험가 배열을 하나씩 순회하며 그룹에 추가한다.

3. 한 그룹의 최대 공포도보다 사람 수가 많아지면, 그룹 하나가 결성된다.

### [문제 풀이](./1.py)

---

### 해설

공포도를 기준으로 오름차순으로 정렬한다. 이후 공포도가 가장 낮은 모험가부터 하나씩 확인하며, 그룹에 포함될 모험가의 수를 계산한다.

만약 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면, 그룹을 결성할 수 있다.

오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 된다. 따라서 최대한 많은 그룹이 구성되는 방법이다.

- 처음 풀이 코드에서 `max`를 사용해 최대 공포도를 계산하였는데, 오름차순으로 정렬이 되었다는 점에서 그룹의 최대 공포도는 현재 확인하는 `i`번째 값이다.

- `max`를 제거하고, 공포도 값을 `arr[i]`로 교체했다.
