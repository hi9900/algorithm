def solution(nums):
    N = len(nums)
    # 폰켓몬의 총 종류
    M = len(set(nums))
    
    answer = min(N // 2, M)
    
    return answer