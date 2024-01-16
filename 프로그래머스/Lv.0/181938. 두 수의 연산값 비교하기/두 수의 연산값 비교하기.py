def solution(a, b):
    x = f'{a}{b}'
    
    return max(int(x), 2*a*b)