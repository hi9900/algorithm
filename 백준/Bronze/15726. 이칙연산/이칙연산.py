import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

result = max(A * B / C, A / B * C)
print(int(result))
