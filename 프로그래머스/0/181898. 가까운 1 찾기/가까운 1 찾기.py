def solution(arr, idx):
    try:
        return idx + arr[idx:].index(1)
    except:
        return -1