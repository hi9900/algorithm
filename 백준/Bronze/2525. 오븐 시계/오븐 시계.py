import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

H, M = divmod(A * 60 + B + C, 60)
if H >= 24:
    H -= 24
print(H, M)
