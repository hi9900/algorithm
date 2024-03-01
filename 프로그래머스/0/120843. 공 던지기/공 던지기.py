def solution(numbers, k):
    cnt = 1
    ball = 0
    while 1:
        if cnt == k:
            return ball+1
        
        ball = (ball + 2) % len(numbers)
        cnt += 1
