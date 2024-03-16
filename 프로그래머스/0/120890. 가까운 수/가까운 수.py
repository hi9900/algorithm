def solution(array, n):
    diff = 101
    answer = 0
    for i in array:
        if abs(n-i) < diff:
            diff = abs(n-i)
            answer = i
        elif abs(n-i) == diff:
            answer = min(i, answer)
    
    return answer