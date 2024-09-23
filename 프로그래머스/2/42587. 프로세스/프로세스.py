from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    count = 0
    while queue:
        i, p = queue.popleft()
        
        # 우선순위가 높은 값이 있으면, 큐에 다시 넣기 
        if any(p < q for (j, q) in queue):
            queue.append((i, p))
        # 방금 꺼낸 프로세스 실행
        else:
            count += 1
            # 찾는 값이면 return
            if location == i:
                return count
    return count
