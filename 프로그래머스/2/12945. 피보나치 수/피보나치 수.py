def solution(n):
    lst = [0] * 100_001
    lst[1] = 1
    for i in range(2, 100_001):
        lst[i] = lst[i-1] + lst[i-2]
    
    return lst[n] % 1234567