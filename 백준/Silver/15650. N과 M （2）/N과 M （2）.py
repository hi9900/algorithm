import sys
input = sys.stdin.readline


# i: 선택한 갯수, k: 현재 원소 인덱스, m: 최종 선택 갯수
def comb(i, k, m):
    if i == m:
        print(*result)
        return
    for j in range(k, N):
        result[i] = lst[j]
        comb(i+1, j+1, m)


N, M = map(int, input().split())
lst = list(range(1, N+1))
result = [0] * M
visited = [0] * N

comb(0, 0, M)

