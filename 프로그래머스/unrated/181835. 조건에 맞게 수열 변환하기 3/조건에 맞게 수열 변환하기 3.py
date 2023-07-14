def solution(arr, k):
    ans = []
    if k % 2:
        for a in arr:
            ans.append(a*k)
    else:
        for a in arr:
            ans.append(a+k)
    return ans