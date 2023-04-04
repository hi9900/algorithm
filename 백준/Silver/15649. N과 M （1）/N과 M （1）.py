import sys
# input = sys.stdin.readline

# i: 선택한 갯수, m: 최종 선택 갯수
def perm(i, m):
    if i == m:
        print(*result)
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            result[i] = lst[j]
            perm(i+1, m)
            visited[j] = 0


N, M = map(int, input().split())
lst = list(range(1, N+1))
result = [0] * M
visited = [0] * N

perm(0, M)

