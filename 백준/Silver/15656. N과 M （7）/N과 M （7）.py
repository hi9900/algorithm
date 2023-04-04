import sys
input = sys.stdin.readline


def perm(i, m):
    if i == m:
        print(*result)
        return
    for j in range(N):
        result[i] = lst[j]
        perm(i+1, m)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = [0] * M
perm(0, M)