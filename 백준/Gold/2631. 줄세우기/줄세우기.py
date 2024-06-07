N = int(input())

arr = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(1, N + 1):
    max_dp = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_dp = max(dp[j], max_dp)
    dp[i] = max_dp + 1

print(N - max(dp))
