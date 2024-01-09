import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = sum(A)
T = sum(B)

print(max(S, T))
