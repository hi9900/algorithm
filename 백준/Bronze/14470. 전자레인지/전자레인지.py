import sys
input = sys.stdin.readline

# 고기온도 A, 목표온도 B, B > A
A = int(input())
B = int(input())
# 언고기, 해동, 안언고기
C = int(input())
D = int(input())
E = int(input())

time = 0
state = A > 0

while 1:
    if A == B:
        break

    # 얼어있고 0 미만 -> C초에 1도씩
    if A < 0:
        A += 1
        time += C
        state = False
    # 얼어있고 0일 때 -> 해동하는 데 D초
    elif A == 0 and not state:
        time += D
        state = True
    # 얼어있지 않을 때 -> E초에 1도씩
    elif A >= 0 and state:
        A += 1
        time += E

print(time)