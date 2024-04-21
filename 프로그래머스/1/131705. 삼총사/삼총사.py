def solve(a, result, number):
    global answer
    
    if len(result) == 3 and sum(result) == 0:
        answer += 1
        return
    
    if len(result) == 3 or a == len(number):
        return
            
    solve(a+1, result+[number[a]], number)
    solve(a+1, result, number)
    

answer = 0
def solution(number):
    global answer
    
    solve(0, [], number)
    return answer