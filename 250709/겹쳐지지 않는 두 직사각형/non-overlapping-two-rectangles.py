n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ps = [[0] * (m+1) for _ in range(n+1)]

# 누적합
for i in range(n):
    for j in range(m):
        ps[i+1][j+1] = ps[i][j+1] + ps[i+1][j] - ps[i][j] + grid[i][j]

# 모든 직사각형 (r1, c1, r2, c2, sum)
rects = []
for i in range(n):
    for j in range(m):
        for i2 in range(i, n):
            for j2 in range(j, m):
                sum_rect = ps[i2+1][j2+1] - (ps[i2+1][j] + ps[i][j2+1] - ps[i][j])
                rects.append((i, j, i2, j2, sum_rect))

# 겹치지 않는 두 직사각형
r = len(rects)
answer = -10e6
for i in range(r):
    rectA = rects[i]
    for rectB in rects[i+1:]:
        if rectA[2] < rectB[0] or rectB[2] < rectA[0] or rectA[3] < rectB[1] or rectB[3] < rectA[1]:
            answer = max(answer, rectA[4] + rectB[4])

print(answer)
