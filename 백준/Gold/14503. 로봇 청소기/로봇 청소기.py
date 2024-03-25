import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dxy = ((-1, 0), (0, 1), (1, 0), (0, -1))
cnt = 0

while 1:
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    else: pass

    # 주변 4 칸 중 빈칸 찾기 > 반시계 방향으로 탐색
    for i in range(4):
        idx = (d - i - 1) % 4
        dx, dy = dxy[idx]

        nx, ny = r + dx, c + dy
        # 3. 빈칸이 있다면, 회전 후 전진
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            r, c, d = nx, ny, idx
            break
    # 2. 빈칸이 없다면, 후진
    else:
        dx, dy = dxy[d]
        bx, by = r - dx, c - dy
        if room[bx][by] == 1:
            print(cnt)
            break

        r, c = bx, by
