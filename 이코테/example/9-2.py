def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
parent = list(range(N+1))

edges = []
result = 0
last = 0

for _ in range(M):
    # A -> B : C
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

# 비용 기준 정렬
edges.sort()

for cost, a, b in edges:
    # 사이클이 발생하지 않으면 == 루트 노드가 다르면 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
        last = cost

# 맨 마지막 cost 제외
print(result - last)
