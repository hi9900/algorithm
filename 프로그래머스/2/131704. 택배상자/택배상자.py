def solution(order):
    N = len(order)
    i = 1   # 메인에서 나올 수 있는 상자
    answer = 0
    
    sub = []
    for o in order:
        # 메인에 o가 있음
        if 0 < i <= o:
            # i ~ o-1까지 sub에 담고, o를 꺼낸다.
            sub += list(range(i, o))
            i = o + 1
            
            if i > N:
                i = 0   # i = 0이면 메인 상자 없음
        # 서브 값이 o
        elif sub and sub[-1] == o:
            sub.pop()
            
        else:
            return answer
        
        answer += 1
        
    return answer