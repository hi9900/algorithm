from itertools import combinations

def solution(nums):
    cnt = 0
    for a, b, c in list(combinations(nums, 3)):
        # 세 수의 합
        check = a + b + c
        
        # 소수 판별
        for i in range(2, check // 2):
            if check % i == 0:
                break
        else:
            cnt += 1
            
    return cnt