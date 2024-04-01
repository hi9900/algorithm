def solution(ingredient):
    answer = 0
    # 1빵 2야채 3고기
    # 1231햄버거
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if stack[len(stack)-4:len(stack)+1] == [1, 2, 3, 1]:
                for _ in range(4):
                    stack.pop()
                answer += 1
    
    return answer