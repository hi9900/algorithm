import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    x, y = map(int, input().split())
    data.append((x, y))

data.sort()
for i in range(N):
    print(*data[i])
