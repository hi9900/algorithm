def solution(emergency):
    n = len(emergency)
    answer = [0] * n
    # 높은 순으로 진료
    sorted_emergency = sorted(emergency, reverse=True)

    for i in range(n):
        answer[i] = sorted_emergency.index(emergency[i]) + 1
        
    
    return answer