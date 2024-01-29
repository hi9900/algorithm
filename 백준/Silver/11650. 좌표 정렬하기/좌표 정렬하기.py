import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    x, y = map(int, input().split())

    data.append((x, y))

data = sorted(data, key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*data[i])
    