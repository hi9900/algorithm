import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

arr = [0] * N
arr[K-1] = sum(lst[0:K])

for i in range(K, N):
    arr[i] = arr[i-1] + lst[i] - lst[i - K]

print(max(arr[K-1:]))
