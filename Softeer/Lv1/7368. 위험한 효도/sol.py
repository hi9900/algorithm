import sys
input = sys.stdin.readline

# 뒤를 돌아볼 때 움직일 수 있음
# 터치 전: a초 뒤, b초 앞
# 터치 후: b초 뒤, a초 앞

a, b, d = map(int, input().split())

time, move = 0, 0
# 터치 전
while 1:
    if move + a >= d:
        time += (d - move)
        move = d
        break
    # 뒤
    time += a
    move += a
    # 앞
    time += b

# 터치 후
while 1:
    if move - b <= 0:
        time += move
        break
    # 뒤
    time += b
    move -= b
    # 앞
    time += a

print(time)