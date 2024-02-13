def solution(land):
    N = len(land)

    data = [[0] * 4 for _ in range(N)]
    data[0] = land[0]
    
    for i in range(1, N):
        for j in range(4):
            data[i][j] = land[i][j] + max(data[i-1][:j] + data[i-1][j+1:])
    
    return max(data[-1])