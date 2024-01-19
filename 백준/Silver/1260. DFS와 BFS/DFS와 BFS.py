from collections import deque
import sys
input = sys.stdin.readline


def DFS(start, data, visited):
    visited[start] += 1
    print(start, end=" ")
    for i in data[start]:
        if visited[i] == 0:
            DFS(i, data, visited)


def BFS(start, data, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in data[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


N, M, V = map(int, input().split())
data = [[] for _ in range(N+1)]
visited = [0] * (N+1)
visited1 = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
for i in range(1, N+1):
    data[i].sort()

DFS(V, data, visited)
print()
BFS(V, data, visited1)
