def solution(n):
    answer = ''
    rule = '412'
    while 1:
        if n == 0:
            break
        n, b = divmod(n, 3)
        answer += rule[b]

        if b == 0:
            n -= 1
    
    return answer[::-1]