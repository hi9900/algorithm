def solution(num_list):
    answer = sum(num_list)
    
    for i in range(len(num_list)):
        if i % 2:
            answer -= num_list[i]
    
    return max(answer, sum(num_list) - answer)