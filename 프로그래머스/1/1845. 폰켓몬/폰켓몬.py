from collections import Counter

def solution(nums):
    N = len(nums)
    
    count = Counter(nums)
    count_keys = len(count.keys())
    
    return min(N/2, count_keys)