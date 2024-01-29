import sys
input = sys.stdin.readline

N = int(input())
data = [list(input().rstrip()) for _ in range(N)]

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
v = [[0] * N for _ in range(N)]
# 총 단지 수
cnt = 0
houses = []
stack = []

for i in range(N):
    for j in range(N):
        if data[i][j] == '1' and v[i][j] == 0:
            v[i][j] = 1
            cnt += 1

            # 단지 내 집수
            house = 1
            stack.append((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in dxy:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == '1' and v[nx][ny] == 0:
                        v[nx][ny] = 1
                        house += 1
                        stack.append((nx, ny))
            houses.append(house)
            house = 0

print(cnt)
houses.sort()
print(*houses, sep="\n")
