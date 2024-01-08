"""
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력 예시
0
2
3
1
2
4
"""

import sys
input = sys.stdin.readline
# 무한을 표현하는 값을 10억으로 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수
N, M = map(int, input().split())
# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(N+1)]
# 방문한 적 있는 지 체크하는 리스트
visited = [False] * (N+1)
# 최단 거리 테이블, 무한으로 초기화
distance = [INF] * (N+1)

# 간선 정보를 입력받기
for _ in range(M):
    # a -> b, 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드의 번호 반환
def get_smalliest_node():
    min_value = INF
    index = 0   # 반환할 노드 인덱스
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    # start에서 출발하는 간선
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(N-1):
        # 현재 최단 거리가 가장 짧은 노드를 방문처리
        now = get_smalliest_node()
        visited[now] = True

        # 선택한 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 기존보다 짧은 경우 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, N+1):
    # 도달할 수 없는 노드는 'INFINITY'로 출력
    print('INFINITY') if distance[i] == INF else print(distance[i])
