N, M, i, j, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = tuple(map(int, input().split()))

dij = ((0, 1), (0, -1), (-1, 0), (1, 0))

dice = [0] * 7  # 주사위 값 초기화(인덱스 = 전개도 번호)
top = 1         # 주사위 윗 면

news = [4, 3, 5, 2]

def update_news(arr, b, d):
    if d == 1:
        return [7 - b, b] + arr[2:]
    if d == 2:
        return [b, 7 - b] + arr[2:]
    if d == 3:
        return arr[:2] + [7 - b, b]
    if d == 4:
        return arr[:2] + [b, 7 - b]


for m in move:
    ni, nj = i + dij[m-1][0], j + dij[m-1][1]

    if 0 <= ni < N and 0 <= nj < M:
        top, news = news[m-1], update_news(news, top, m)
        bottom = 7 - top

        if board[ni][nj] == 0:
            board[ni][nj] = dice[bottom]
        else:
            dice[bottom], board[ni][nj] = board[ni][nj], 0

        i, j = ni, nj
        print(dice[top])

    else:
        continue
