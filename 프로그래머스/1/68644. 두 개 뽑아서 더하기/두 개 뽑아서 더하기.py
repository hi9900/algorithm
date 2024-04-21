def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            answer.add(numbers[i]+j)
    
    return sorted(list(answer))