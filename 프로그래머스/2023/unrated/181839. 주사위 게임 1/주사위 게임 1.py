def solution(a, b):
    if (a+b) % 2:
        return 2*(a+b)
    elif (a*b) % 2:
        return a**2 + b**2
    else:
        return abs(a-b)