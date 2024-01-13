from collections import deque

N = int(input())
# 진입 차수 초기화
indegree = [0] * (N+1)
# 간선 정보 연결 리스트
graph = [[] for _ in range(N+1)]

time = [0] * (N+1)

# i번 강의 -> 강의 시간, 선수강의번호, -1
for i in range(1, N+1):
    t, *arr = map(int, input().split())
    time[i] = t

    # x번 강의 -> i번 강의
    for x in arr:
        if x == -1:
            break

        graph[x].append(i)
        indegree[i] += 1


# 위상 정렬
def topology():
    # 알고리즘 수행 결과를 담을 리스트
    result = [t for t in time]
    q = deque()

    # 진입차수가 0
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            # 수강 시간 = 선수강의시간 + 강의시간
            result[i] = max(result[i], result[now] + time[i])

            # now와 연결된 노드 제거
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(*result[1:], sep="\n")


topology()
