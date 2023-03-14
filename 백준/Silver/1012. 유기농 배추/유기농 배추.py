#import sys
#input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    data = [[0]*(M+2) for _ in range(N+2)]
    checked = [[0] * (M+2) for _ in range(N+2)]
    for _ in range(K):
        x, y = map(int, input().split())
        data[y+1][x+1] = 1

    dij = ((-1, 0), (0, -1), (1, 0), (0, 1))
    cnt = 0
    stack=[]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if data[i][j] == 1 and checked[i][j] == 0:
                
                stack.append((i, j))
                cnt += 1
                while stack:
                    ii, jj = stack.pop()
                    checked[ii][jj] = cnt
                    for di, dj in dij:
                        ni, nj = ii+di, jj+dj
                        if data[ni][nj] == 1 and checked[ni][nj] == 0:
                            stack.append((ni, nj))


    print(cnt)
