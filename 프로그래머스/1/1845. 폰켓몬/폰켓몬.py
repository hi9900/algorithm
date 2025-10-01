def solution(nums):
    N = len(nums)
    count = len(set(nums))
    return min(N/2, count)