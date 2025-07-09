n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def isPositive(si, sj, ei, ej):
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            if grid[i][j] <= 0:
                return -1

    return (ei-si+1) * (ej-sj+1)

answer = -1
for si in range(n):
    for sj in range(m):
        for ei in range(si, n):
            for ej in range(sj, m):
                # 사각형 내부 판정
                answer = max(answer, isPositive(si, sj, ei, ej))

print(answer)
