import sys
input = sys.stdin.readline

import heapq

N = int(input())
data = []
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(data) == 0:
            print(0)
        else:
            # 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거
            print(-heapq.heappop(data))
    else:
        # 배열에 x를 추가
        heapq.heappush(data, -x)
