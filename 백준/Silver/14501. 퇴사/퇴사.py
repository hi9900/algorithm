def dfs(n, result):
    global ans

    if n >= N:
        ans = max(ans, result)
        return

    if n+data[n][0] <= N:
        dfs(n+data[n][0], result+data[n][1])
    dfs(n+1, result)


N = int(input())
data = []
for _ in range(N):
    T, P = map(int, input().split())
    data.append((T, P))

ans = 0
dfs(0, 0)
print(ans)