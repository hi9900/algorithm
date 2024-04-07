def solution(s):
    answer = ''
    
    i = 0
    for c in s:
        if c == ' ':
            i = 0
            answer += c
            continue
            
        if i % 2 == 0:
            answer += c.upper()
        else:
            answer += c.lower()
        i += 1
        
    return answer