import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

sum_i = 0
min_i = N+1
for i in range(M, N+1):
    if (i**(0.5)) == int(i**(0.5)):
        min_i = min(min_i, i)
        sum_i += i

print(-1) if sum_i == 0 else print(sum_i, min_i, sep="\n")
