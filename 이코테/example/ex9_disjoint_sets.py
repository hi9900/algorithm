# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # x가 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합 합치기 union
def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 부모가 큰 노드를 작은 노드의 부모로 설정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = list(range(v+1))

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 출력
print('부모 테이블:', *parent[1:])
