from collections import deque

# 상하좌우 방향벡터
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(x, y):
    global grid, visited
    queue = deque([(x, y)])
    # 1. 현재 노드 방문 처리
    visited[x][y] = True

    # 3. 큐가 빌 때까지 반복
    while queue:
        # 2-1. 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        print(x, y)
        # 2-2. 인접한 노드를 방문
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


# 2차원 배열 예제 (1은 갈 수 있는 경로, 0은 갈 수 없는 경로)
grid = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
]

# 방문 정보
visited = [[False] * len(grid[0]) for _ in range(len(grid))]

# BFS 함수 호출
bfs(0, 0)
