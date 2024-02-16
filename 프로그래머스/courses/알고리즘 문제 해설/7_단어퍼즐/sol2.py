def solution(strs, t):
    N = len(t)
    
    MAX = 20001
    dp = [MAX] * (N) + [0] * 5
    
    for i in range(N, -1, -1):
        for j in range(5):
            if i + j >= N:
                break
            
            if t[i:i+j+1] in strs:
                dp[i] = min(dp[i], dp[i+j+1] + 1)

    return dp[0] if dp[0] != MAX else -1