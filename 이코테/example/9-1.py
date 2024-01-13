N, M = map(int, input().split())

# 부모 테이블 (초기 = 본인)
team = list(range(N+1))


# x의 루트 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 팀 합치기
def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    
    # 작은 노드를 큰 노드의 부모로
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


for _ in range(M):
    x, a, b = map(int, input().split())

    # 팀 합치기 수행
    if x == 0:
        union(team, a, b)

    # 같은 팀 여부 확인
    elif x == 1:
        # 루트 노드가 같으면, 같은 팀
        if find_parent(team, a) == find_parent(team, b):
            print('YES')
        else:
            print('NO')

