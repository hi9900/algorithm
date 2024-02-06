def solution(box, n):
    ans = 1
    for i in box:
        ans *= i // n
    answer = ans
    return answer