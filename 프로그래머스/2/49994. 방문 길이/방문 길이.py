def solution(dirs):
    move = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    
    # 점이 아닌 선 기준
    visited = list([0] * 11 for _ in range(11))
    v = set()
    
    i, j = 5, 5
    answer = 0
    # for v in visited:
    #     print(v)
    
    for dir in dirs:
        di, dj = move[dir]
        ni, nj = i + di, j + dj
        
        if 0 <= ni < 11 and 0 <= nj < 11:
            if (i, j, ni, nj) not in v:
                v.add((i, j, ni, nj))
                v.add((ni, nj, i, j))
                answer += 1

            i, j = ni, nj
    return answer