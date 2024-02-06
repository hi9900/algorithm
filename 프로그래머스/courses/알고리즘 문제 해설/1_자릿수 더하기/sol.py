def solution(n):
    answer = 0
    while n:
        n, a = divmod(n, 10)
        answer += a
        
    return answer