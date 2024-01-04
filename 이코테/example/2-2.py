N, M = map(int, input().split())

tmp = 1
# 각 행의 최솟값과 비교한 큰 값
for i in range(N):
    data = list(map(int, input().split()))
    tmp = max(min(data), tmp)

print(tmp)
