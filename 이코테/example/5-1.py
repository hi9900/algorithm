N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 상하좌우
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

"""
1. 얼음틀을 순회하며 구멍(0)을 발견한다.
2. 구멍에서부터 상하좌우로 연결된 구멍을 체크한다.(DFS)
3. 더 이상 구멍이 없다면, 아이스크림 +1  
    얼음틀을 다시 순회하며, 체크안된 구멍을 체크(계속)
"""


def check(x, y):
    for di, dj in dxy:
        ni = x + di
        nj = y + dj
        if ni < 0 or nj < 0 or ni >= N or nj >= M:
            continue

        if board[ni][nj] == '0' and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            check(ni, nj)


cnt = 0
for i in range(0, N):
    for j in range(0, M):
        # 구멍이 뚫려있고 체크한 적 없으면
        if board[i][j] == '0' and visited[i][j] == 0:
            visited[i][j] = 1
            check(i, j)
            cnt += 1

print(cnt)


"""
4 5
00110
00011
11111
00000

3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

8
"""
