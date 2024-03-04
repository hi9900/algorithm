def solution(order):
    N = len(order)
    # 보조 컨테이너 벨트는 선입후출 > stack
    stack = []
    
    result = 0
    main = 1
    for i in range(N):
        # 1. 꺼낼 수 있는 보조를 확인한다.
        if stack and order[i] == stack[-1]:
            stack.pop()
            result += 1
            continue
            
        # 2. 남은 메인을 확인한다.
        # 2-1. 남은 메인에는 실어야 할 상자가 없음
        if main > order[i]:
            return result
        # 2-2. 메인에는 실어야 할 상자가 있고, 
        # 그 상자가 나올 때까지 보조로 이동
        # 현재 메인 ~ order[i]-1 까지의 상자가 보조로 이동한다.
        else:
            stack += list(range(main, order[i]))
            main = order[i] + 1
            result += 1
    return result