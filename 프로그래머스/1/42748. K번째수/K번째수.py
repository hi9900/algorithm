def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sortedArray = sorted(array[i-1:j])
        answer.append(sortedArray[k-1])
        
    return answer