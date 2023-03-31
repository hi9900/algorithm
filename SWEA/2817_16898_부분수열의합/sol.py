import sys
sys.stdin = open("input.txt")


def solution(i, n, sm, k):
    global cnt
    if i == n:
        if sm == k:
            cnt += 1
        return

    solution(i+1, n, sm+data[i], k)
    solution(i+1, n, sm, k)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = 0
    solution(0, N, 0, K)
    print(f"#{tc} {cnt}")
