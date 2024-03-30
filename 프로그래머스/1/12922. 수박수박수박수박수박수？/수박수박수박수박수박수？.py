def solution(n):
    answer = '수박'
    if n == 0:
        return ''
    if n == 1:
        return '수'
    
    if n % 2:
        return answer * (n//2) + '수'
    
    return answer * (n//2)