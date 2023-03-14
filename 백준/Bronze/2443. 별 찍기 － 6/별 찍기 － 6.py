import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, 0, -1):
    ans = " " * (N-i) + "*" * (2*i-1)
    print(ans)

