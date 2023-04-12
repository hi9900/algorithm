import sys
input = sys.stdin.readline
import heapq

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

result = data[0]
for i in range(1, N):
    for j in range(N):
        heapq.heappush(result, data[i][j])
        heapq.heappop(result)

print(heapq.heappop(result))
