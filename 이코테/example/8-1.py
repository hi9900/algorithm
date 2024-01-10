import pprint
# 회사 N개, 경로 M개
N, M = map(int, input().split())

"""
# 플로이드 워셜
모든 경로에 대한 최소 비용 계산
graph[i][j] = i -> j 로 가는 최소 비용
"""
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신 i -> i
for i in range(N+1):
    graph[i][i] = 0

# 연결된 경로 비용은 1, 양방향
for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

# a -> b 로 바로 이동하는 경우 = graph[a][b]
# a -> b 의 경로에서 k번 노드를 거쳐 가는 경우 = graph[a][k] + graph[k][b]
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

X, K = map(int, input().split())

# 1 -> K 최소 시간 + K -> X 최소 시간
result = graph[1][K] + graph[K][X]
print(-1) if result >= INF else print(result)