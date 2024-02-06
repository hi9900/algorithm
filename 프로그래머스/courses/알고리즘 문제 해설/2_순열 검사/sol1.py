def solution(arr):
    nums = [0] * (100001)
    
    # 빈도 체크
    for num in arr:
        if nums[num] >= 1:
            return False
        nums[num] += 1
        
    # 검사
    for i in range(1, len(arr)+1):
        if nums[i] != 1:
            return False

    return True