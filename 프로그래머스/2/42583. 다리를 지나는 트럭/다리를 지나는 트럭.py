from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    sum_bridge = 0
    
    count = 0
    while trucks:
        count += 1
        sum_bridge -= bridge.popleft()
        
        if sum_bridge + trucks[0] <= weight:
            # 트럭을 다리에 올린다.
            truck = trucks.popleft()
            bridge.append(truck)
            sum_bridge += truck
        else:
            bridge.append(0)
        
    # 마지막 트럭이 건널 때 까지 기다리기
    count = count + bridge_length
    return count
