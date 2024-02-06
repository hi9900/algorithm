def solution(board):
    R = len(board)
    C = len(board[0])
    
    # 최댓값
    max_b = 0
    
    # 경계를 표시하기 위해 +1
    dp = [[0] * (C+1) for _ in range(R+1)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 1:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                max_b = max(dp[i+1][j+1], max_b)
    
    return max_b**2