import sys
input = sys.stdin.readline


def sol(a, M):
    if a == M:
        print(*s)
        return

    for i in range(s[a-1], N):
        s[a] = data[i]
        sol(a+1, M)

N, M = map(int, input().split())

data = list(x for x in range(1, N+1))
s = [0] * M

sol(0, M)

