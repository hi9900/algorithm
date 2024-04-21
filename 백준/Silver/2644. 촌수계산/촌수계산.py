import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
parent = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    parent[y] = x

v = [0] * (N+1)
q = deque()
q.append((a, 0))

while q:
    i, cnt = q.popleft()
    v[i] = 1

    if i == b:
        print(cnt)
        break

    # i의 부모
    if v[parent[i]] == 0:
        q.append((parent[i], cnt+1))
    # i의 자식
    for child in graph[i]:
        if v[child] == 0:
            q.append((child, cnt+1))
else:
    print(-1)