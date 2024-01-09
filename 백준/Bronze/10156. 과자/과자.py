import sys
input = sys.stdin.readline

K, N, M = map(int, input().split())
pay = K * N
print(0) if pay < M else print(pay - M)