import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, 2*N+1):
    if i % 2:
        ans = "* " * N
        print(ans[:N])
    else:
        ans = " *" * N
        print(ans[:N])