import sys
sys.stdin = open('input.txt', 'r')


def solve(si, sj, a):
    global tmp
    tmp[si][sj] = a
    dij = ((1, 0), (0, 1))
    x = board[si][sj]

    for di, dj in dij:
        ni, nj = si + x * di, sj + x * dj
        if 0 <= ni < N and 0 <= nj < N and tmp[ni][nj] == -1:
            solve(ni, nj, a+1)


for _ in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    tmp = [[-1] * N for _ in range(N)]
    solve(0, 0, 0)
    print('YES' if tmp[N-1][N-1] != -1 else 'NO')