# 시간초과

from collections import deque 

def solution(strs, t):
    N = len(t)
    answer = 20001
    
    q = deque()
    # 시작 인덱스, depth, 맞춘 str
    q.append((0, 0, ""))
    
    while q:
        i, d, s = q.popleft()
        if s == t:
            answer = min(answer, d)
            break
            
        if d >= answer:
            continue
            
        for str in strs:
            n = len(str)
            if t[i:i+n] == str:
                q.append((i+n, d+1, s+str))

    if answer == 20001:
        return -1

    return answer