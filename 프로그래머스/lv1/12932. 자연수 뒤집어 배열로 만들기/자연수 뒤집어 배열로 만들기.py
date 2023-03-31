def solution(n):
    answer = list(str(n))
    answer = [int(x) for x in answer]
    return answer[::-1]