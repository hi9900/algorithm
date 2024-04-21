import sys
input = sys.stdin.readline


# 1. 미세먼지 확산
def move_dust(_room):
    global clean
    dust = [[0] * C for _ in range(R)]
    dij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(R):
        for j in range(C):
            now = _room[i][j]
            if now == 0 or now == -1:
                continue

            if now < 5:
                dust[i][j] += now
                continue

            cnt = 0
            move = now // 5
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) != clean[0] and (ni, nj) != clean[1]:
                    cnt += 1
                    dust[ni][nj] += move

            dust[i][j] += (now - move * cnt)
    return dust


# 2. 공청기 작동
def clean_dust(start, _room):
    dust = [[0] * C for _ in range(R)]
    dij_u = ((0, 1), (-1, 0), (0, -1), (1, 0))  # 우 상 좌 하
    dij_d = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상

    i, j = start[0]
    for di, dj in dij_u:
        while 1:
            ni, nj = i + di, j + dj
            if (ni, nj) == start[0]:
                break
            if 0 <= ni < R and 0 <= nj < C:
                dust[ni][nj] += _room[i][j]
                i, j = ni, nj
            else:
                break

    i, j = start[1]
    for di, dj in dij_d:
        while 1:
            ni, nj = i + di, j + dj
            if (ni, nj) == start[1]:
                break
            if 0 <= ni < R and 0 <= nj < C:
                dust[ni][nj] += _room[i][j]
                i, j = ni, nj
            else:
                break

    for i in range(1, R-1):
        for j in range(1, C-1):
            if i != start[0][0] and i != start[1][0]:
                dust[i][j] += _room[i][j]

    return dust


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 0. 공기청정기 위치 > 항상 1열
clean = []
for i in range(R):
    if room[i][0] == -1:
        clean.append((i, 0))
        clean.append((i+1, 0))
        break

for _ in range(T):
    room = clean_dust(clean, move_dust(room))

result = 0
for i in room:
    result += sum(i)

print(result)