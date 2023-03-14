import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    ans = "*" * (i+1)
    print(ans)
for i in range(N):
    ans = "*" * (N-i-1)
    print(ans)