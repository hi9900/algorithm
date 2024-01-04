N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

board = [[999] * M for _ in range(N)]

dij = [(-1, 0), (0, -1), (1, 0), (0, 1)]

board[0][0] = 1
stack = [(0, 0, 1)]

while stack:
    i, j, step = stack.pop()

    if maze[i][j] == 1:
        for di, dj in dij:
            ni, nj = i + di, j + dj
            # 범위 밖
            if ni < 0 or nj < 0 or ni >= N or nj >= M:
                continue
            # 다음 값이 1이고, 이동 횟수가 크면 작은걸로 수정
            if maze[ni][nj] == 1 and board[ni][nj] > step+1:
                board[ni][nj] = step+1
                stack.append((ni, nj, step+1))

print(board[N-1][M-1])
