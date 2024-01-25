import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [0] * K
for _ in range(K):
    lst[_] = int(input())

lst.sort()
# 항상 K <= N

def solution(s, e, lst, N, result):
    if s > e:
        return result

    mid = (s+e) // 2

    # mid의 길이로 잘랐을 때 갯수
    cnt = 0
    for i in lst:
        cnt += i // mid
    # 넉넉하면 더 높게
    if cnt >= N:
        result = max(result, mid)
        return solution(mid + 1, e, lst, N, result)

    # 모자르면 더 낮게
    else:
        return solution(s, mid-1, lst, N, result)

print(solution(1, max(lst), lst, N, 0))