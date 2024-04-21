from collections import Counter

def solution(s):
    answer = ''
    for i in Counter(s):
        if Counter(s)[i] == 1:
            answer += i
    
    return ''.join(sorted(answer))