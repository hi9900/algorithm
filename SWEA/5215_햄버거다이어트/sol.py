import sys
sys.stdin = open("input.txt")


def solution(i, N, kcal, L, sm):
    global result

    if kcal > L:
        return

    if i == N:
        result = max(result, sm)
        return

    solution(i+1, N, kcal+data[i][1], L, sm+data[i][0])
    solution(i+1, N, kcal, L, sm)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    solution(0, N, 0, L, 0)
    print(f"#{tc} {result}")
