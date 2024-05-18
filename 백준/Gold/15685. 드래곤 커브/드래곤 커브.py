N = int(input())
board = [[0] * 101 for _ in range(101)]
dxy = ((0, 1), (-1, 0), (0, -1), (1, 0))

for _ in range(N):
    x, y, d, g = map(int, input().split())

    # 1. 드래곤 커브 선 방향 구하기
    curve = [d]
    for i in range(1, g+1):
        tmp = []
        for c in curve[::-1]:
            next_curve = (c + 1) % 4
            tmp.append(next_curve)
        curve = curve + tmp

    # 2. 드래곤 커브 그리기
    board[y][x] = 1
    for c in curve:
        dy, dx = dxy[c]
        nx, ny = x + dx, y + dy
        board[ny][nx] = 1
        x, y = nx, ny

# 3. 정사각형 확인
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] == 1:
            cnt += 1

print(cnt)
