def solution(sticker):
    answer = 0
    
    N = len(sticker)
    n = N // 2
    
    if N == 1:
        return sticker[0]
    
    # 첫 번째 스티커를 뜯는 경우
    dp = [0] * N
    dp[0] = sticker[0]
    dp[1] = dp[0]
    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    answer = dp[N-2]
    
    # 첫 번째 스티커를 뜯지 않는 경우
    dp = [0] * N
    dp[1] = sticker[1]
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    answer = max(answer, dp[N-1])
    
    return answer