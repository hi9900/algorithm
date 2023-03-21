import sys
input = sys.stdin.readline
n, m = map(int, input().split())

data = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    i -=1
    j -=1
    for x in range((j-i)//2+1):
        data[i+x], data[j-x] = data[j-x], data[i+x]
print(*data)
