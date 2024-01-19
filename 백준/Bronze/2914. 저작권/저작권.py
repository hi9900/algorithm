import sys
input = sys.stdin.readline

A, I = map(int, input().split())
# I = X / A -> X = A * I
# 894 / 38 A = 23.53 -> 24 I

print((I-1) * A + 1)
