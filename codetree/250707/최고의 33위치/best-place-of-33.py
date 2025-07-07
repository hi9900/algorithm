n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n - 3 + 1):
    for j in range(n - 3 + 1):
        coin = 0
        for di in range(3):
            for dj in range(3):
                coin += grid[i + di][j + dj]
        ans = max(ans, coin)

print(ans)
