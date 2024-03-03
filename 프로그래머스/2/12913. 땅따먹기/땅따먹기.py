def solution(land):
    answer = 0
    # 행의 개수 N
    N = len(land)
    
    d = [[0] * 4 for _ in range(N)]
    d[0] = land[0]

    for i in range(1, N):
        for j in range(4):
            # land[i][j] + d[i-1][j]를 제외한 값들 중 큰 값
            # d[i-1][:j] + d[i-1][j+1:] -> max 계산을 위해 빈 리스트 없애기
            d[i][j] = land[i][j] + max(d[i-1][:j] + d[i-1][j+1:])
            
    return max(d[N-1])