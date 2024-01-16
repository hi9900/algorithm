def solution(arr, delete_list):
    for num in delete_list:
        while num in arr:
            arr.remove(num)
    return arr