def solution(my_string):
    answer = []
    for c in my_string:
        if c.isnumeric():
            answer.append(int(c))
    answer.sort()
    return answer