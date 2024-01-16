def solution(my_string, is_suffix):
    n = len(my_string)
    m = len(is_suffix)
    if my_string[n-m:] == is_suffix:
        return 1
    return 0