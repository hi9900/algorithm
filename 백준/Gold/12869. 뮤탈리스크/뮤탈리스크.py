from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline


def solve():
    global q, V
    while q:
        scv, c = q.popleft()

        for attack in perm:
            new_arr = [scv[i] - attack[i] if scv[i] - attack[i] > 0 else 0 for i in range(N)]
            # 모든 체력이 0이하이면, 종료
            if sum(new_arr) == 0:
                return c+1

            # 더 적은 횟수로 도착
            if new_arr not in V:
                q.append((new_arr, c + 1))
                V.append((new_arr))


N = int(input())
arr = list(map(int, input().split()))

# (9, 3, 1)으로 나타낼 수 있는 순열
perm = tuple(permutations((9, 3, 1)[:N], N))
V = []

q = deque([(arr, 0)])
print(solve())
