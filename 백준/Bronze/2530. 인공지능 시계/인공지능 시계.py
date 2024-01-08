import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
D = int(input())

C += D
if C >= 60:
    up, C = divmod(C, 60)
    B += up

if B >= 60:
    up, B = divmod(B, 60)
    A += up

if A >= 24:
    up, A = divmod(A, 24)

print(A, B, C)
