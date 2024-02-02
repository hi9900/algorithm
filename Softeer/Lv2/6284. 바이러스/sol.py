import sys
input = sys.stdin.readline

K, P, N = map(int, input().split())
# 1초당 P배
# N초 -> P ** N배
# K * pow(P, N)
for i in range(1, N+1):
    K *= P
    K %= 1_000_000_007

print(K)
