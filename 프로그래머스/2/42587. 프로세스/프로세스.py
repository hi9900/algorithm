from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    cnt = 0
    while q:
        # q 안에 든 가장 높은 우선순위
        max_q = max(q)[0]
        
        if q[0][0] < max_q:
            q.rotate(-1)
        else:
            p, i = q.popleft()
            cnt += 1
            if i == location:
                return cnt
