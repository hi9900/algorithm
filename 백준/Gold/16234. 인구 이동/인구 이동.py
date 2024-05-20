def move(union, total, cnt):
    global world
    people = total // cnt
    for ui, uj in union:
        world[ui][uj] = people


def bfs():
    v = [[0] * N for _ in range(N)]
    dij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    check = 0

    p = []
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                check += 1
                p.append((i, j, check))
                v[i][j] = check

                total_world, cnt_world = 0, 0
                union_world = []

                while p:
                    ii, jj, c = p.pop()
                    total_world += world[ii][jj]
                    cnt_world += 1
                    union_world.append((ii, jj))
                    for di, dj in dij:
                        ni, nj = ii + di, jj + dj
                        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and L <= abs(world[ii][jj] - world[ni][nj]) <= R:
                            v[ni][nj] = c
                            p.append((ni, nj, c))

                if cnt_world >= 2:
                    move(union_world, total_world, cnt_world)

    return check == N * N


N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
result = 0

while 1:
    a = bfs()

    if a:
        break
        
    result += 1


print(result)
