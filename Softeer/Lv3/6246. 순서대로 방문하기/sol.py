import sys
input = sys.stdin.readline


def dfs(start, target_cnt):
    x, y = start

    # 모든 타겟을 방문했다면, 종료
    if target_cnt == m:
        result.append(1)
        return
        
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        # 타겟에 도달했다면, 타겟 변경
        if (nx, ny) == target[target_cnt] and v[nx][ny] == 0 :
            v[nx][ny] = 1
            dfs((nx,ny), target_cnt+1)
            v[nx][ny] = 0
        
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0 and v[nx][ny] == 0:
            v[nx][ny] = 1
            dfs((nx, ny), target_cnt)
            v[nx][ny] = 0


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]

target = []
for _ in range(m):
    x, y = map(int, input().split())
    target.append((x-1, y-1))

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
result = []
start = target[0]
v[start[0]][start[1]] = 1
dfs(start, 1)

print(result.count(1))
