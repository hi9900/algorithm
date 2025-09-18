import heapq

# 도시 N, 통로 M, 시작 C
N, M, C = map(int, input().split())

# 도시와 통로 정보
graph = [[] for _ in range(N+1)]
# C에서 index 까지의 최단 거리
distance = [1e9] * (N+1)

for _ in range(M):
    # X -> Y : Z
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


# C에서 모든 도시까지의 최소 거리 -> 다익스트라
def dijkstra(start):
    # 우선순위 큐
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 우선순위 큐에서 하나 씩 뽑아서 확인
        dist, now = heapq.heappop(q)

        # 처리된 적 있다 == 최단 거리가 초기값(무한)이 아니다.
        # 처리된 적 있고, 현재 고려하는 거리보다 짧으면 갱신하지 않음
        if distance[now] < dist:
            continue

        # now와 연결된 통로 확인
        for n, c in graph[now]:
            # start -> now -> n
            cost = dist + c
            # now를 거쳐서 n으로 가는 경우가 더 짧으면,
            # 그 거리로 갱신하고, 우선순위 큐에 삽입
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))


dijkstra(C)

cnt, time = 0, 0
for d in distance:
    # 무한이 아니면, 해당 도시에 전보 가능
    # 무한이 아닌 값들 중에서 최댓값이 전체 걸리는 시간
    if d < 1e9:
        cnt += 1
        time = max(time, d)

print(cnt - 1, time)
