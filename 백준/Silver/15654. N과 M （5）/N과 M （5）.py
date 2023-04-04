import sys
input = sys.stdin.readline

def perm(i, m):
    if i == m:
        print(*result)
        return
    for j in range(N):
        if not visited[j]:
            result[i] = lst[j]
            visited[j] = 1
            perm(i+1, m)
            visited[j] = 0


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = [0] * M
visited = [0] * N

perm(0, M)