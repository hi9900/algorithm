import sys
input = sys.stdin.readline


def perm(i, k, m):
    if i == m:
        print(*result)
        return
    for j in range(k, N):
        result[i] = lst[j]
        perm(i+1, j, m)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = [0] * M
perm(0, 0, M)