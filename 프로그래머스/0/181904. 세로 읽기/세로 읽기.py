def solution(my_string, m, c):
    answer = ''
    N = len(my_string)
    for i in range(N // m):
        answer += my_string[i * m + c - 1]
    return answer