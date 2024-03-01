def solution(n):
    # factorial
    d = [0] * 12
    d[0] = 1
    d[1] = 1
    for i in range(1, 12):
        d[i] = i * d[i-1]
        if d[i] > n:
            return i-1
