import sys
sys.stdin = open("input.txt")

T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 양끝 0을 추가 -> 실제 인덱스 +1
    # 아래에서 출발(2)
    sj = data[99].index(2)
    si = 99
    ii, jj = si, sj

    visited = [[0] * 102 for _ in range(100)]
    # 좌 우 위
    dij = ((0, -1), (0, 1), (-1, 0),)

    while ii != 0:
        visited[ii][jj] = 1
        for di, dj in dij:
            ni, nj = ii+di, jj+dj
            if data[ni][nj] == 1 and visited[ni][nj] == 0:
                ii, jj = ni, nj

    print(f"#{tc} {jj - 1}")
