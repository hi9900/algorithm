def solution(s):
    arr = list(s.split())
    
    answer = 0
    for i in range(len(arr)):
        if arr[i] == 'Z':
            answer -= int(arr[i-1])
            continue
        answer += int(arr[i])
        
    return answer