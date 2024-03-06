def solution(picks, minerals):
    # picks = dia, iron, stone 곡괭이 수
    
    piro = {
        0: {'diamond': 1, 'iron': 1, 'stone': 1},
        1: {'diamond': 5, 'iron': 1, 'stone': 1},
        2: {'diamond': 25, 'iron': 5, 'stone': 1},
    }
    N = len(minerals)
    
    # 광물을 5개 단위로 나누고 곡괭이의 개수만큼만 선택
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]
    
    # 광물을 다이아몬드, 철, 돌의 개수에 따라 내림차순으로 정렬 
    # ?? -> 곡괭이를 순서대로 쓰려고 
    minerals.sort(key=lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)
    
    answer = 0
    for mineral in minerals:
        for i in range(3):
            if picks[i]:
                picks[i] -= 1
                use = i
                break
        
        for m in mineral:
            answer += piro[use][m]
    return answer