import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    T, P = map(int, input().split())
    data.append((T, P))

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    if i + data[i][0] <= N:
        dp[i] = max(dp[i + data[i][0]] + data[i][1], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])