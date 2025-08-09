import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] = (dp[i-1] + (dp[i - m] if i-m >= 0 else 0)) % 1_000_000_007

print(dp[n])