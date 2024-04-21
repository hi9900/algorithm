import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2. 모래 이동
left_tornado = [
    [0, 0, 0.02, 0, 0],
    [0, 0.10, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.10, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
up_tornado = list(zip(*left_tornado))
down_tornado = list(reversed(list(zip(*left_tornado))))
right_tornado = list(reversed(list(zip(*down_tornado))))

tornados = {
    0: left_tornado,
    1: down_tornado,
    2: right_tornado,
    3: up_tornado
}

# 1. 토네이도 이동
# 좌 하 우 상
dij = ((0, -1), (1, 0), (0, 1), (-1, 0),)


def move_sand(x, y, _d):
    tornado = tornados[_d]

    sand = arr[x][y]
    out = 0

    for i in range(-2, 3):
        for j in range(-2, 3):
            ni, nj = x + i, y + j
            move = int(sand * tornado[2+i][2+j])
            arr[x][y] -= move

            if move and 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += move
            else:
                out += move

    # a 위치로 남은 모래 이동
    di, dj = dij[_d]
    if 0 <= x+di < N and 0 <= y+dj < N:
        arr[x+di][y+dj] += arr[x][y]
    else:
        out += arr[x][y]

    arr[x][y] = 0
    return out


# 1 1 2 2 3 3 ... N-1 N-1 N-1
r, c = N // 2, N // 2

times, turn = 1, 0
d = 0
# 3. 빠진 모래 더하기
result = 0
for i in range(1, N):
    cnt = 2
    if i == N-1:
        cnt = 3
    for j in range(cnt):
        for k in range(i):
            di, dj = dij[d]
            r, c = r+di, c+dj
            # print(r, c)
            if arr[r][c]:
                result += move_sand(r, c, d)

        d = (d + 1) % 4

print(result)
