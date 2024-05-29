N, D = map(int, input().split())
arr = list(tuple(map(int, input().split())) for _ in range(N))

dp = list(range(D+1))

arr.sort(key=lambda x: (x[0], x[1], x[2]))

before = 0
for a in arr:
    start, end, d = a
    if end > D:
        continue

    dp[end] = min(dp[end], dp[start] + d)

    for i in range(end+1, D+1):
        dp[i] = min(dp[i], dp[end] + i - end)

print(dp[-1])
