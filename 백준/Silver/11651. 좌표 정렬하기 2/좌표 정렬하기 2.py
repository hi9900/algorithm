import sys
input = sys.stdin.readline

N = int(input())
num = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    num[_] = [a, b]

num.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(*num[i])
