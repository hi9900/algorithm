import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 트럭
time = 1
q = deque([[arr[0], 1]])
i = 1

while q:
    time += 1
    # 다리를 건너는 트럭은 최소 하나
    if q[0][1] + 1 > W:
        q.popleft()

    # 다리 위 무게
    bridge = 0
    for a in q:
        a[1] += 1
        bridge += a[0]

    # 다음 트럭
    if i < N and bridge + arr[i] <= L:
        q.append([arr[i], 1])
        i += 1

print(time)
