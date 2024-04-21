answer = []
check = False

def dfs(a, tickets, V):
    global answer, check
    
    # 모든 티켓을 사용하면 끝
    if sum(V) == len(tickets):
        check = True
        return answer
    
    for i in range(len(tickets)):
        if V[i] == 0 and tickets[i][0] == a:
            V[i] = 1
            answer.append(tickets[i][1])
            dfs(tickets[i][1], tickets, V)
            
            # 재귀 종료 조건
            if check:
                return answer
            
            V[i] = 0
            answer.pop()
            
def solution(tickets):
    global answer
    # 티켓 사용 여부
    V = [0] * len(tickets)
    
    tickets.sort(key=lambda x: (x[0], x[1]))
    answer.append('ICN')
    dfs('ICN', tickets, V)
    return answer