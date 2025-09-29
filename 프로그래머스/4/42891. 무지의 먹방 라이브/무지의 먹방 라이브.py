import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같으면
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_time = 0    # 총 소요 시간
    prev = 0        # 이전에 먹은 음식 시간
    n = len(food_times) # 남은 음식의 개수

    while q:
        time, now = q[0]
        if (time - prev) * n <= k - sum_time:
            heapq.heappop(q)
            sum_time += (time - prev) * n
            n -= 1
            prev = time
        else:
            sorted_q = sorted(q, key=lambda x: x[1])
            return sorted_q[(k-sum_time) % n][1]
            
