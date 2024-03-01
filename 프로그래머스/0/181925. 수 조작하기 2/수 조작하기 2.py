def solution(numLog):
    N = len(numLog)
    result = ''
    for i in range(1, N):
        tem = numLog[i] - numLog[i-1]
        if tem == 1:
            result += 'w'
        elif tem == -1:
            result += 's'
        elif tem == 10:
            result += 'd'
        else:
            result += 'a'
    return result