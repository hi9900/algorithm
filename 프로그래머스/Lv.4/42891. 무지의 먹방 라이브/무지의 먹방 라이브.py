import heapq

def solution(food_times, k):
    # k초 전에 다먹음
    if sum(food_times) <= k:
        return -1
    
    q = []
    # (음식 시간, 음식 번호)의 형태로 큐에 삽입
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) 
    
    # 먹는 데 사용한 시간
    sum_t = 0
    # 직전에 다 먹은 음식 시간
    prev = 0
    # 남은 음식 개수
    n = len(food_times)
    
    # 먹은 시간 + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수
    while sum_t + (q[0][0] - prev) * n <= k:
        # 현재 음식 시간
        now = heapq.heappop(q)[0]

        # 현재 음식을 먹는 데 걸리는 시간 = (현재 시간 - 이전 시간) * 현재 음식 개수 
        sum_t += (now - prev) * n
        n -= 1
        
        prev = now
        
    # 남은 음식을 번호 순으로 확인
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_t) % n][1]
        