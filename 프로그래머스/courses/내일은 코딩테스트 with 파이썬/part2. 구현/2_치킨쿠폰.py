def solution(chicken):
    answer = 0
    r = 0

    # 10씩 나눈 몫을 더하기
    while chicken:
        chicken, a = divmod(chicken, 10)
        answer += chicken
        r += a
        
    # 쿠폰의 쿠폰도 고려하기
    while r >= 10:
        r, b = divmod(r, 10)
        answer += r
        r += b
        
    return answer