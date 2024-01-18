import sys
input = sys.stdin.readline

# A, B, C = 5분(300초), 1분(60초), 10초
# 각각이 배수이므로, 그리디
T = int(input())
if T % 10:
    print(-1)
else:
    a, T = divmod(T, 300)
    b, T = divmod(T, 60)
    c, T = divmod(T, 10)

    print(a, b, c)