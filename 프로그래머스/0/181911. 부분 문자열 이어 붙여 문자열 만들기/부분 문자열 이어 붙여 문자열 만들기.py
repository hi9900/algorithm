def solution(my_strings, parts):
    answer = ''
    n = len(my_strings)
    
    for i in range(n):
        s, e = parts[i]
        string = my_strings[i]
        
        answer += string[s:e+1]
    
    return answer