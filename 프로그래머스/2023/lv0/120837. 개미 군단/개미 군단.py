def solution(hp):
    result= 0
    for att in [5, 3, 1]:
        a, hp = divmod(hp, att)
        result += a
    return result