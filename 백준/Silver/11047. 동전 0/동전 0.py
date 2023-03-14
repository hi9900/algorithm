import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dong = [0] * N
for _ in range(N):
    A = int(input())
    dong[_] = A
cnt = 0
for d in dong[::-1]:
    if K // d:
        cnt += K//d
        K %= d
print(cnt)