import sys
input = sys.stdin.readline


# # i: 선택한 갯수, k: 현재 원소 인덱스, m: 최종 선택 갯수
def comb(i, k, m):
    if i == m:
        print(*result)
        return
    for j in range(k, N):
        result[i] = lst[j]
        comb(i+1, j+1, m)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = [0] * M

comb(0, 0, M)