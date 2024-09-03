def solution(citations):
    citations.sort(reverse=True)
    N = len(citations)
    answer = 0
    
    for i in range(N):
        h = citations[i]
        
        if h > answer:
            answer = i + 1
        else:
            return answer
        
    return answer