import sys
input = sys.stdin.readline
n, m = map(int, input().split())

data = [0] * n

for _ in range(m):
    s, e, b = map(int, input().split())
    for i in range(s-1, e):
        data[i] = b
print(*data)


