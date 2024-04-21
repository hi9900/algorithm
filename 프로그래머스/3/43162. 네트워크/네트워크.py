from collections import deque

def solution(n, computers):
    answer = 0
    V = [0] * n
    q = deque([])
    
    for i in range(n):
        if V[i] == 0:
            answer += 1
            q.append(i)
            V[i] = 1
            
            while q:
                i = q.popleft()
                for j in range(n):
                    if i != j and computers[i][j] == 1 and V[j] == 0:
                        V[j] = 1
                        q.append(j)
    
    return answer