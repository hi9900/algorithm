import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    ans = " " * i + "*" * (2*N-1 -2*i)
    print(ans)

for i in range(N-2, -1, -1):
    ans = " " * i + "*" * (2 * N - 1 - 2 * i)
    print(ans)