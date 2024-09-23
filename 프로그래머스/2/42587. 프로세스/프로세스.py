from collections import deque

def solution(priorities, location):
    q = list(enumerate(priorities))
    count = 0
    
    while q:
        count += 1
        N = len(q)
        run_i, run_p, idx = *q[0], 0
        
        for j in range(N):
            i, p = q[j]
            # 우선순위가 더 높은 프로세스 저장
            if run_p < p:
                idx = j
                run_i, run_p = i, p
                
        # 프로세스 실행 (큐에서 삭제)
        q = q[idx+1:] + q[:idx]
        
        # 찾는 프로세스이면, 값 반환
        if run_i == location:
            return count

    return count
