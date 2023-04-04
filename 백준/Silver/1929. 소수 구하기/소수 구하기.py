import sys
input = sys.stdin.readline

M, N = map(int, input().split())

# [0, 1 = False] + [2 ~ N]
a = [False, False] + [True] * (N-1)

# 1부터 N까지
for i in range(N+1):
    if a[i]:
        for j in range(2*i, N+1, i):
            a[j] = False

for i in range(M, N+1):
    if a[i]:
        print(i)
