def solution(my_string):
    answer = [0] * 52
    for c in my_string:
        ord_c = ord(c)
        if ord_c <= 90:
            answer[ord_c - 65] += 1
        else:
            answer[ord_c - 97 + 26] += 1
    return answer