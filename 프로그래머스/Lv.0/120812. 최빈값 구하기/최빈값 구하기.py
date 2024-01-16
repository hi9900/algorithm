def solution(array):
    answer = [0] * (max(array) + 1)
    for i in array:
        answer[i] += 1
        
    max_x = max(answer)
    if answer.count(max_x) > 1:
        return -1

    return answer.index(max_x)