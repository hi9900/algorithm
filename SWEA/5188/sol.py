import sys
sys.stdin = open("input.txt")


def minmin(ii, jj, ans):
    global result
    if ans >= result:
        return

    if (ii, jj) == (N, N):
        result = min(result, ans)

    for di, dj in dij:
        ni, nj = ii + di, jj + dj
        if data[ni][nj]:
            minmin(ni, nj, ans + data[ni][nj])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    # print(data)

    # 아래 오른쪽
    dij = ((1, 0), (0, 1))
    result = 10e9

    minmin(1, 1, data[1][1])
    print(f"#{tc} {result}")
