import sys
input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [True] * (N+1)
if N >= 0:
    is_prime[0] = False
if N >= 1:
    is_prime[1] = False

for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, N+1, i):
            is_prime[j] = False

for k in range(M, N+1):
    if is_prime[k]:
        print(k)
