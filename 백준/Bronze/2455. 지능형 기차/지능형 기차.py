import sys
input = sys.stdin.readline

data = [0] * 5
for i in range(1, 5):
    a, b = map(int, input().split())
    data[i] = data[i-1] - a + b

print(max(data))
