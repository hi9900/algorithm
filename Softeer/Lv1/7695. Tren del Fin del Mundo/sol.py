import sys
input = sys.stdin.readline

N = int(input())

# 가장 남쪽에 있는 점 = y 좌표가 가장 작은 좌표
result = [1001, 1001]
for _ in range(N):
    x, y = map(int, input().split())

    if y < result[1]:
        result = [x, y]

print(*result)