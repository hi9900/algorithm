import sys
input = sys.stdin.readline

m, n = map(int, input().split())

is_prime = [1] * (n+1)

is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(n**(1/2))+1):
    if is_prime[i]:
        for j in range(i**2, n+1, i):
            is_prime[j] = 0

for i in range(m, n+1):
    if is_prime[i]:
        print(i)
