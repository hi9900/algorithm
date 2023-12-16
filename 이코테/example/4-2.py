# N, M = map(int, input().split())
# A, B, d = map(int, input().split())
#
# data = [list(map(int, input().split())) for _ in range(N)]
N, M = 4, 4
A, B, d = 1, 1, 0
data = [
    [1, 1, 1, 1], [1, 0, 0, 1],
    [1, 1, 0, 1], [1, 1, 1, 1]
]

visited = list([0] * M for _ in range(N))
visited[A][B] = 1
cnt = 1


while 1:
    # 네 방향
    for i in range(4):
        #  왼쪽 방향: 북 동 남 서 -> 왼, 아래, 오, 위
        fst = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        dx, dy = fst[d]
        nx, ny = A + dx, B + dy

        # nx, ny는 맵 안
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 가보지 않았고, 육지
        if visited[nx][ny] == 0 and data[nx][ny] == 0:
            A, B, d = nx, ny, d
            visited[nx][ny] = 1
            cnt += 1
            break

        else:
            d = (d+1) % 4

    else:
        # 뒤로 한 칸: 북, 동, 남, 서 -> 아래, 왼, 위, 오
        back = [(-1, 0), (0, -1), (1, 0), (0, +1)]
        bx, by = back[d]
        nx, ny = A + bx, B + by

        if nx < 0 or nx >= N or ny < 0 or ny >= M or data[nx][ny] == 1:
            break

        A, B = nx, ny

print(cnt)
