import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    ans = "*" * (i+1) + " " * (2*N-2*(i+1)) + "*" * (i+1)
    print(ans)
for i in range(N-2, -1, -1):
    ans = "*" * (i+1) + " " * (2*N-2*(i+1)) + "*" * (i+1)
    print(ans)