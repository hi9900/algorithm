def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        for s, index in stack:
            answer[index] += 1
        
        while stack and stack[-1][0] > prices[i]:
            stack.pop()
        
        stack.append((prices[i], i))
        
    return answer