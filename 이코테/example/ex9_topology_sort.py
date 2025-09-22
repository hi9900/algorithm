from collections import deque


# 위상 정렬
def topology_sort():
    # 수행 결과를 담을 리스트
    result = []
    q = deque()

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 수행
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # now와 연결된 노드들의 진입 차수 -1
        for i in graph[now]:
            indegree[i] -= 1

            # 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    print(*result)


# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
# 진입 차수 초기화
indegree = [0] * (v+1)
# 간선 정보를 담을 연결 리스트
graph = [[] for _ in range(v+1)]

# 간선 정보 입력
for _ in range(e):
    # a -> b
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입 차수 +1
    indegree[b] += 1

topology_sort()
