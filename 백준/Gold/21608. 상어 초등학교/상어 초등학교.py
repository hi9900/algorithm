# 학생 번호, 좋아 하는 학생 리스트
def sit_down(idx, lst):
    global board
    check = []

    for i in range(N):
        for j in range(N):
            like_cnt = 0
            empty_cnt = 0

            if board[i][j] != 0:
                continue

            for di, dj in dij:
                if 0 <= i + di < N and 0 <= j + dj < N:
                    # 인접한 좋아 하는 학생 수
                    if board[i+di][j+dj] in lst:
                        like_cnt += 1
                    # 인접한 빈 자리 수
                    elif board[i+di][j+dj] == 0:
                        empty_cnt += 1

            check.append((like_cnt, empty_cnt, i, j))

    check.sort(key=lambda x: (-x[0], -x[1], x[2], x[3],))
    board[check[0][2]][check[0][3]] = idx


N = int(input())
board = [[0] * N for _ in range(N)]
dij = ((-1, 0), (1, 0), (0, -1), (0, 1))

graph = []

for _ in range(N ** 2):
    p, *like = map(int, input().split())
    graph.append([p, like])
    sit_down(p, like)


graph.sort()
result = 0
like_sum = (0, 1, 10, 100, 1000)

# 만족도 조사
for i in range(N):
    for j in range(N):
        like_cnt = 0
        for di, dj in dij:
            if 0 <= i + di < N and 0 <= j + dj < N:
                if board[i + di][j + dj] in graph[board[i][j] - 1][1]:
                    like_cnt += 1

        result += like_sum[like_cnt]

print(result)