import sys
input = sys.stdin.readline


def perm(i, k, m):
    global ans
    if i == m:
        if tuple(result) not in ans:
            print(*result)
            ans.add(tuple(result))
        return
    for j in range(k, N):
        result[i] = lst[j]
        perm(i+1, j, m)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = [0] * M
visited = [0] * N
ans = set()
perm(0, 0, M)