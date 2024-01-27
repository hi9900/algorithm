import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]  # N X M

# 맨 왼쪽 위칸이
# 흰색인 경우
white = 0
# 검은색인 경우
black = 0

result = N * M

si, sj = 0, 0
while 1:
    white, black = 0, 0
    for i in range(si, si+8):
        for j in range(sj, sj+8):
            if (i + j) % 2 == 0:
                if board[i][j] == "W":
                    black += 1
                else:
                    white += 1
            else:
                if board[i][j] == "W":
                    white += 1
                else:
                    black += 1
    result = min(result, white, black)

    sj += 1
    if sj > M - 8:
        sj = 0
        si += 1
    if si > N - 8:
        break

print(result)