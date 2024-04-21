def solution(x):
    sum_x = sum(map(int, str(x)))
    return False if x % sum_x else True