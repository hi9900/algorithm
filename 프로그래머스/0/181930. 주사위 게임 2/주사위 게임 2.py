def solution(a, b, c):
    answer = 0
    
    if len(set((a, b, c))) == 1:
        return (3 * a) * (3 * a ** 2) * (3 * a ** 3)
    elif len(set((a, b, c))) == 3:
        return a + b + c
    return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)