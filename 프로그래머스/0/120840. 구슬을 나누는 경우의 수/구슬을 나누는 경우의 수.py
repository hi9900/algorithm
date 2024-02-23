def solution(balls, share):
    if balls // 2 < share:
        share = balls - share

    # (balls) C (share)
    a, b = 1, 1
    for i in range(share):
        a *= balls
        b *= share
        balls -= 1
        share -= 1
        
    return a // b
        