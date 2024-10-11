def solution(n, lost, reserve):
    answer = 0
    std = [1] * n
    
    for i in lost:
        std[i-1] -= 1
    for i in reserve:
        std[i-1] += 1
    
    for i in range(n):
        if std[i] == 0:
            # 앞번호
            if i > 0 and std[i-1] > 1:
                std[i-1] -= 1
                std[i] += 1
                answer += 1
            # 뒷번호
            elif i < n-1 and std[i+1] > 1:
                std[i+1] -= 1
                std[i] += 1
                answer += 1
        else:
            answer += 1
    
    return answer