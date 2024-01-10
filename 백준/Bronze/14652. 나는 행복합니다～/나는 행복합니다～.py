import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

print(*divmod(K, M))