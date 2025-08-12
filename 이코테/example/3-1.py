n = input()

# 좌표는 8 x 8 (1~8, a~h)
l = ["a", "b", "c", "d", "e", "f", "g", "h"]

# 나이트의 좌표
si, sj = int(n[1]) - 1, l.index(n[0])

# 이동할 수 있는 경우
dij = ((-2, -1), (-2, 1), (2, -1), (2, 1),
       (-1, -2), (-1, 2), (1, -2), (1, 2))

cnt = 0
for di, dj in dij:
    ni, nj = si + di, sj + dj

    if 0 <= ni < 8 and 0 <= nj < 8:
        cnt += 1

print(cnt)
