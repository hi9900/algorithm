import sys
input = sys.stdin.readline

S, T, D = map(int, input().split())

# 1. 두 기차는 h시간 후에 만난다. (D는 2*S의 배수)
h = D // (S * 2)

# 2. 파리의 이동 거리
F = h * T

print(F)