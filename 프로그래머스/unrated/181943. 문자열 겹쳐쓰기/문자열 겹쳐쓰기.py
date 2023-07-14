def solution(my_string, overwrite_string, s):
    n = len(overwrite_string)
    return my_string[:s] + overwrite_string + my_string[s+n:]