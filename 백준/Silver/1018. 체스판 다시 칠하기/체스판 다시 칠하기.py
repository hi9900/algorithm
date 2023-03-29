import sys
input = sys.stdin.readline


def chess(a, b):
    c = board[a][b]
    draw = 0
    draw1 = 0
    for x in range(a, a+8):
        for y in range(b, b+8):
            if (x+y) % 2 == (a+b) % 2:
                if board[x][y] != c:
                    draw += 1
                else:
                    draw1 += 1
            else:
                if board[x][y] == c:
                    draw += 1
                else:
                    draw1 += 1
    return draw, draw1


N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
result = []
for i in range(N-7):
    for j in range(M-7):
        d1, d2 = chess(i, j)
        result.append(min(d1, d2))

print(min(result))