def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        result = 1000001
        for i in arr[s:e+1]:
            if i > k:
                result = min(result, i)
        if result == 1000001:
            answer.append(-1)
        else:
            answer.append(result)
        
    return answer