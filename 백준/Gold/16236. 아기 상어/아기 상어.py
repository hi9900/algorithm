import sys
from collections import deque
input = sys.stdin.readline


# 현재 위치에서, 크기보다 작은 물고기까지의 거리
def go_fish():
    q = deque([(sx, sy)])
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    dxy = ((-1, 0), (1, 0), (0, 1), (0, -1))

    while q:
        xx, yy = q.popleft()
        for dx, dy in dxy:
            nx, ny = xx + dx, yy + dy
            if 0 <= nx < N and 0 <= ny < N and baby >= board[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[xx][yy] + 1
                q.append((nx, ny))

    return dist


def eat_fish(dist):
    # 밥 물고기 위치, 거리
    x, y, min_d = 0, 0, 10e9

    for i in range(N):
        for j in range(N):
            # 먹을 수 있으면,
            if board[i][j] and dist[i][j] != -1 and baby > board[i][j]:
                if dist[i][j] < min_d:
                    x, y, min_d = i, j, dist[i][j]

    if min_d == 10e9:
        return False
    return x, y, min_d


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 아기 상어의 위치
        if board[i][j] == 9:
            sx, sy = i, j
            board[i][j] = 0


baby = 2    # 아기 상어의 크기
answer = 0  # 총 이동 거리
food = 0    # 먹은 물고기

while 1:
    check = eat_fish(go_fish())
    
    if not check:
        print(answer)
        break

    sx, sy = check[0], check[1],
    answer += check[2]
    board[sx][sy] = 0
    food += 1

    if food >= baby:
        baby += 1
        food = 0