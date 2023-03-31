import sys
sys.stdin = open("input.txt")


def solution(n, ii, jj, num):
    if n == 7:
        ans.add(num)
        return

    dij = ((-1, 0), (0, -1), (1, 0), (0, 1),)
    for di, dj in dij:
        ni, nj = ii + di, jj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            solution(n+1, ni, nj, num*10+board[ni][nj])


T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            solution(1, i, j, board[i][j])

    result = len(ans)
    print(f"#{tc} {result}")

