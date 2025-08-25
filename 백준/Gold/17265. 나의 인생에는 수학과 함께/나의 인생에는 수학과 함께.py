import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def calc(num1, op, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    return num1 * num2


# 현재값 cur, 연산자 op
def dfs(i, j, cur, op):
    global N, data, max_v, min_v
    
    # 현재 칸 계산
    cell = data[i][j]
    if cell in '+-*':
        op = cell
    else:
        num = int(cell)
        if cur is None:
            cur = num
        else:
            cur = calc(cur, op, num)
            op = None

    # 도착 시 값 갱신
    if i == N - 1 and j == N - 1:
        max_v = max(max_v, cur)
        min_v = min(min_v, cur)
        return

    # 이동: 아래, 오른쪽
    dij = ((1, 0), (0, 1),)
    for di, dj in dij:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            dfs(ni, nj, cur, op)


N = int(input())
data = [input().split() for _ in range(N)]

max_v, min_v = -10e6, 10e6

dfs(0, 0, None, None)
print(max_v, min_v)
