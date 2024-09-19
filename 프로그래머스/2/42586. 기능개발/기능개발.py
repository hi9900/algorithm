from collections import deque
import math
def solution(progresses, speeds):
    N = len(progresses)
    q = deque([])
    answer = []
    
    for i in range(N):
        # 남은 일수 계산
        day = (100 - progresses[i]) / speeds[i]
        q.append(math.ceil(day))
    
    # 배포될 기능
    fn = 1
    prev = q.popleft()
    while q:
        if q[0] <= prev: # 함께 배포
            q.popleft()
            fn += 1
        else:
            answer.append(fn)
            prev = q.popleft()
            fn = 1

    if len(q) == 0:
        answer.append(fn)
        
    return answer