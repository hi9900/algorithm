def solution(n):
    answer = set()
    
    for i in range(2, n+1):
        # 소수 검사
        for j in range(2, int(i**(0.5))+1):
            if i % j == 0:
                break
        # 인수 검사
        else:
            # 최대한 나누기
            while 1:
                a, b = divmod(n, i)
                # 나눌수 없거나, 인수가 아니면 종료
                if a == 0 or b != 0:
                    break
                n = a
                answer.update([i])
    return sorted(list(answer))