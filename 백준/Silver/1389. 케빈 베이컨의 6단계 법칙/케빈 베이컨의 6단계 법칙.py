from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())

    graph[A].append(B)
    graph[B].append(A)

q = deque()
cnt = (M+1) * (N+1)
answer = 0
# i에서 j까지 가는 최단 경로 d 찾기
for i in range(1, N+1):
    q.append((i, 0))
    V = [0] * (N + 1)

    while q:
        j, d = q.popleft()
        for k in graph[j]:
            if k != i and V[k] == 0:
                V[k] = d+1
                q.append((k, d+1))

    if sum(V) < cnt:
        cnt = sum(V)
        answer = i
print(answer)
