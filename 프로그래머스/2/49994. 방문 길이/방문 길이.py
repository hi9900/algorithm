def solution(dirs):
    move = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    
    v = set()
    i, j = 0, 0
    answer = 0

    for dir in dirs:
        di, dj = move[dir]
        ni, nj = i + di, j + dj
        
        if -5 <= ni <= 5 and -5 <= nj <= 5:
            if (i, j, ni, nj) not in v:
                v.add((i, j, ni, nj))
                v.add((ni, nj, i, j))
                answer += 1

            i, j = ni, nj
            
    return answer