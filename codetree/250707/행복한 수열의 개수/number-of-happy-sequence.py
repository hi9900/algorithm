n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def is_happy(seq, M):
    prev = seq[0]
    cnt = 1

    if cnt >= M:
        return True

    for x in seq[1:]:
        if x == prev:
            cnt += 1
        else:
            prev = x
            cnt = 1
        if cnt >= M:
            return True
    return False

answer = 0
# 각 행 검사
for i in range(n):
    if is_happy(grid[i], m):
        answer += 1

# 각 열 검사
for j in range(n):
    col = [grid[i][j] for i in range(n)]
    if is_happy(col, m):
        answer += 1
    
print(answer)