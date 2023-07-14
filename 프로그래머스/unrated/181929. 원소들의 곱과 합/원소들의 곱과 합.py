def solution(num_list):
    m = 1
    for i in num_list:
        m *= i
    return 0 if m > sum(num_list)**2 else 1