import sys
# input = sys.stdin.readline


def bfs(start, c):
    global result
    q = []
    v = set()

    q.append(start)
    v.add(start)

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1),):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < m:
                if (ni, nj) not in v and data[ni][nj] == 1:
                    data[ni][nj] = c
                    q.append((ni, nj))
                    v.add((ni, nj))
    # print(len(v))
    # print(v)
    result = max(result, len(v))


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
c = 1
result = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            c += 1
            data[i][j] = c
            bfs((i, j), c)

# print(data)
print(c-1)
print(result)
