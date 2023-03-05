import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

sum_a = 0
for i in range(K):
    sum_a += data[i]
sum_max = sum_a

for i in range(K, N):
    sum_a = sum_a + data[i] - data[i-K]
    sum_max = max(sum_a, sum_max)

print(sum_max)
