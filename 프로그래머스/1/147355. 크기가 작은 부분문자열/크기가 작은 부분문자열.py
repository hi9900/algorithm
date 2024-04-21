def solution(t, p):
    answer = 0
    n = len(p)
    check = list(t[:n])

    if int(''.join(check)) <= int(p):
        answer += 1
    
    for i in range(n, len(t)):
        check.pop(0)
        check.append(t[i])
        
        if int(''.join(check)) <= int(p):
            answer += 1
    
    return answer