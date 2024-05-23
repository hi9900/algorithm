def color_cnt(color, start):
    cnt = 0
    if start == 'f':
        for ball in balls:
            if ball == color:
                cnt += 1
            else:
                return cnt
    else:
        for ball in balls[::-1]:
            if ball == color:
                cnt += 1
            else:
                return cnt


N = int(input())
balls = input()

# 앞 / 뒤에서 부터 같은 색 공의 갯수
front_color = color_cnt(balls[0], 'f')
back_color = color_cnt(balls[-1], 'b')

f_ball = balls.count(balls[0])
b_ball = balls.count(balls[-1])

result = 0
if f_ball == b_ball == N:
    pass
elif balls[0] == balls[-1]:
    result = min(f_ball - max(front_color, back_color), N - f_ball)
else:
    result = min(f_ball - front_color, b_ball - back_color)

print(result)