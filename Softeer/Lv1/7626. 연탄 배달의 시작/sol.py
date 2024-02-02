import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# 두 마을의 거리 차이
dist = 10e6
cnt = 0

for i in range(1, N):
    if lst[i] - lst[i-1] < dist:
        cnt = 1
        dist = lst[i] - lst[i-1]
    elif lst[i] - lst[i-1] == dist:
        cnt += 1

print(cnt)