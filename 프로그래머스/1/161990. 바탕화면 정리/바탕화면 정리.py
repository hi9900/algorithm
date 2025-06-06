def solution(wallpaper):
    N = len(wallpaper)
    M = len(wallpaper[0])
    
    min_i = min_j = 10e9
    max_i = max_j = -1
    
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == '#':
                min_i = min(min_i, i)
                min_j = min(min_j, j)
                max_i = max(max_i, i)
                max_j = max(max_j, j)
    
    return [min_i, min_j, max_i+1, max_j+1]
