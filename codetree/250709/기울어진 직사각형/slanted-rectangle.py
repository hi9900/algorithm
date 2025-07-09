n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dij = ((-1, 1, 1), (-1, -1, 2), (1, -1, 3), (1, 1, 4))
answer = 0
for i in range(n):
    for j in range(n):
        for k1 in range(1, n + 1):
            for k2 in range(1, n + 1):
                r, c = i, j
                rect = 0

                for di, dj, idx in dij:
                    isBreak = 0

                    if idx % 2:
                        dd = k1
                    else:
                        dd = k2

                    for d in range(dd):
                        ni, nj = r + di * d, c + dj * d
                        if 0 <= ni < n and 0 <= nj < n:
                            rect += grid[ni][nj]
                        else:
                            isBreak = 1
                            break
                    if isBreak:
                        break
                    # 다음 꼭짓점
                    r, c = r + di * dd, c + dj * dd

                else:
                    answer = max(answer, rect)

print(answer)