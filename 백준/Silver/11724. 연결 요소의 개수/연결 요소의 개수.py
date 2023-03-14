import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    data[u].append(v)
    data[v].append(u)

cnt = 1
stack = []

for _ in range(1, N+1):
    if visited[_] == 0:
        visited[_] = cnt
        stack.append(_)
        while stack:
            x = stack.pop()
            for i in data[x]:
                if visited[i] == 0:
                    visited[i] = cnt
                    stack.append(i)

        cnt += 1
print(cnt-1)