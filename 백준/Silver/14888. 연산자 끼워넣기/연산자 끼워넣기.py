import sys
from itertools import permutations
input = sys.stdin.readline


def calc(x, y, c):
    if c == 0:
        return x + y
    if c == 1:
        return x - y
    if c == 2:
        return x * y
    if c == 3:
        if x >= 0:
            return x // y
        return -(-x // y)


N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_a, min_a = -10e9, 10e9

"""
1. 연산자를 나열
2. arr 사이에 끼워 넣는다.
3. 가장 큰 / 작은 결과를 저장한다.
"""

# 1. + - x // 로 변환한 리스트
operators = []
for i in range(4):
    if operator[i]:
        operators += [i] * operator[i]
# 2
for p in (permutations(operators, N-1)):
    result = arr[0]
    for i in range(N-1):
        result = calc(result, arr[i+1], p[i])
    # 3
    max_a = max(max_a, result)
    min_a = min(min_a, result)

print(max_a)
print(min_a)
