def solution(n):
    rule = '412'
    
    answer = ''
    while n > 0:
        n, b = divmod(n, 3)
        if b == 0:
            n -= 1
        answer += rule[b]
    
    return answer[::-1]