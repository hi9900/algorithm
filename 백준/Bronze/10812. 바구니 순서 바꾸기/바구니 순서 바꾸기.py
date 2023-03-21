import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(range(1, N+1))

for _ in range(M):
    i, j, k = map(int, input().split())
    data[i-1:j] = data[k-1:j] + data[i-1:k-1]
print(*data)