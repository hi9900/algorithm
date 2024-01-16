def solution(n):
    if n % 2:
        return sum(list(range(1, n+1, 2)))
    return sum(list(map(lambda x: x**2, list(range(2, n+1, 2)))))
   

