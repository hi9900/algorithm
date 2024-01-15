import sys
input = sys.stdin.readline

M = int(input())
N = int(input())


sum_n = 0
min_n = 10_001

for i in range(M, N+1):
    if i == 1:
        continue
        
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sum_n += i
        min_n = min(min_n, i)

print(-1) if sum_n == 0 else print(sum_n, min_n, sep="\n")
