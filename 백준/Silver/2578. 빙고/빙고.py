import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(5)]
data_t = list(map(list, zip(*data)))
num = []
for _ in range(5):
    num += list(map(int, input().split()))
num = num[::-1]
cnt = 0
check = []

while num:
    say = num.pop()
    cnt += 1

    for i in range(5):
        for j in range(5):
            if data[i][j] == say:
                say = 0
                data[i][j] = 0
                data_t[j][i] = 0
                break
        if say == 0:
            break

    # 빙고 검사
    # 가로, 세로, 대각 이어진 0이 5개
    bingo = 0
    dea = 0
    dea_t = 0
    for i in range(5):
        if sum(data[i]) == 0:
            bingo += 1
        if sum(data_t[i]) == 0:
            bingo += 1

        dea += data[i][i]
        dea_t += data[i][4-i]
    if dea == 0:
        bingo += 1
    if dea_t == 0:
        bingo += 1

    if bingo >= 3:
        print(cnt)
        break