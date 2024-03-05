def calc(numbers, i, sum_n, target):
    global result
    
    if i == len(numbers):
        if sum_n == target:
            result += 1
        return
    
    calc(numbers, i+1, sum_n + numbers[i], target)
    calc(numbers, i+1, sum_n - numbers[i], target)

def solution(numbers, target):
    global result
    result = 0
    
    arr = []
    calc(numbers, 0, 0, target)

    return result
    
