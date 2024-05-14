import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

data = [0] * (N+1)
data[1] = arr[0]
for i in range(2, N+1):
    data[i] = arr[i-1] + data[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(data[j] - data[i-1])