import heapq
import sys
sys.stdin = open('ex8_dijkstra_input.txt')
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
N, M = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드와 간선에 대한 정보를 담을 리스트
graph = [[] for _ in range(N+1)]
# 최단거리 테이블 초기화
distance = [INF] * (N+1)

# 간선 정보 입력
for _ in range(M):
    # a -> b: 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단거리가 짧은 노드
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있으면, 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 노드 확인
        for n, c in graph[now]:
            cost = dist + c
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

dijkstra(start)

for i in range(1, N+1):
    print('INFINITY') if distance[i] == INF else print(distance[i])

"""
출력 예시
0
2
3
1
2
4
"""