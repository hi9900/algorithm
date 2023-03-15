import sys
input = sys.stdin.readline

N = int(input())
data = [[0]*(N+2)]+[[0] + list(map(int, input().rstrip())) + [0] for _ in range(N)] + [[0]*(N+2)]
visited = [[0]*(N+2) for _ in range(N+2)]

stack = []
cnt = 0
nums = []
dij = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i in range(1, N+1):
    for j in range(1, N+1):
        if data[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            stack.append((i, j))
            num = 0
            while stack:
                ii, jj = stack.pop()
                if visited[ii][jj] == 0:
                    num += 1
                    visited[ii][jj] = cnt
                    for di, dj in dij:
                        ni, nj = ii+di, jj+dj
                        if data[ni][nj] == 1 and visited[ni][nj] == 0:
                            stack.append((ni, nj))
            nums.append(num)

nums.sort()
print(cnt, *nums, sep="\n")
