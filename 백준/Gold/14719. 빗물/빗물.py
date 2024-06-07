H, W = map(int, input().split())
blocks = list(map(int, input().split()))

board = []
for block in blocks:
    tmp = [0] * (H - block) + [1] * block
    board.append(tmp)

board = list(zip(*board))
result = 0

for i in range(H):
    cnt = 0
    isBlock = False
    for j in range(W):
        if not isBlock and board[i][j] == 1:
            isBlock = True
            continue
        if isBlock and board[i][j] == 0:
            cnt += 1
            continue
        if isBlock and board[i][j] == 1:
            result += cnt
            cnt = 0

print(result)