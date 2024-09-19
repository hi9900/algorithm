def solution(s):
    answer = 0
    
    for el in s:
        if el == "(":
            answer += 1
            continue
    
        answer -= 1
        if answer < 0:
            return False
            
    return True if answer == 0 else False