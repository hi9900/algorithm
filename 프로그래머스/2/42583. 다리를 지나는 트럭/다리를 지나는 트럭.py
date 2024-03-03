from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    N = len(truck_weights)
    bridges = deque()
    
    # 트럭 무게, 경과 시간
    bridges.append([truck_weights[0], 1])
    i = 1
    
    while bridges:
        answer += 1
        sum_b = 0
        for bridge in bridges:
            bridge[1] += 1
            sum_b += bridge[0]
            
        if bridges[0][1] > bridge_length:
            sum_b -= bridges.popleft()[0]
            
        if i < N and sum_b + truck_weights[i] <= weight:
            bridges.append([truck_weights[i], 1])
            i += 1
            
    return answer