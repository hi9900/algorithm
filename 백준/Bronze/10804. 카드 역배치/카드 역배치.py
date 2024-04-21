import sys
input = sys.stdin.readline

data = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    data[a:b+1] = data[b:a-1:-1]

print(*data[1:])