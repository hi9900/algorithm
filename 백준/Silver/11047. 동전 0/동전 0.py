import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [0] * N
for _ in range(N):
    A[_] = int(input())

cnt = 0

for i in range(N-1, -1, -1):
    if A[i] > K:
        continue

    if K == 0:
        break

    n, K = divmod(K, A[i])
    cnt += n

print(cnt)