n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [
    [(0, 0), (0, 1), (-1, 0)], [(0, 0), (0, 1), (0, 2)]
]

# 시계방향 90도 회전: (x, y) -> (y, -x)
def rotate(block):
    return [(y, -x) for x, y in block]

# 좌우 반전: (x, y) -> (x, -y)
def reflect(block):
    return [(x, -y) for x, y in block]

# (0, 0)을 기준으로 최소값 이동
def nomalize(block):
    min_x = min(x for x, y in block)
    min_y = min(y for x, y in block)
    return sorted([(x - min_x, y - min_y) for x, y in block])

# 모든 블록 형태 저장
shapes = set([])
for block in blocks:
    s = block[:] # 원본 유지
    for _ in range(4):
        s = rotate(s)
        r = reflect(s)

        shapes.add(tuple(nomalize(s)))
        shapes.add(tuple(nomalize(r)))

shapes = list(shapes)
answer = 0

def solve(shape, i, j):
    total = 0
    for di, dj in shape:
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < m:
            total += grid[ni][nj]
        else:
            return 0
    return total


for shape in shapes:
    for i in range(n):
        for j in range(m):
            answer = max(answer, solve(shape, i, j))
            
print(answer)