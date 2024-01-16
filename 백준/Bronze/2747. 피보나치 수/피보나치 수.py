import sys
input = sys.stdin.readline

d = [0] * 46
d[1] = 1

N = int(input())

for i in range(2, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])