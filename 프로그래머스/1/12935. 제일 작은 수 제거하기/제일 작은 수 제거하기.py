def solution(arr):
    min_i = arr.index(min(arr))
    arr.pop(min_i)
    
    if arr == []:
        return [-1]
    return arr