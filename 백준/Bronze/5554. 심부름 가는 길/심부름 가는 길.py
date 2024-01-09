import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())

# 집 -> 학교 -> PC방 -> 학원
x, y = divmod(A + B + C + D, 60)
print(x)
print(y)
