import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def sol(room):
    v[room] = 1

    for i, j in graph[room]:
        if not v[i]:
            d[i] = d[room] + j
            sol(i)


N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

d = [0] * (N + 1)
v = [0] * (N + 1)

sol(1)
print(max(d))
