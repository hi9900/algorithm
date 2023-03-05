# https://www.acmicpc.net/problem/2615
import sys
import pprint as pp
input = sys.stdin.readline


def gase(data):
    global win
    for i in range(19):
        cnt = 1
        winij.clear()
        for j in range(1, 19):
            if data[i][j] != 0 and data[i][j - 1] == data[i][j]:
                cnt += 1
                winij.append([i+1, j])
            else:
                if cnt == 5:
                    win = data[i][j - 1]
                    break
                cnt = 1
                winij.clear()
        else:
            if cnt == 5:
                win = data[i][j - 1]
                break

        if win != 0:
            break


def dea(data):
    global win
    for j in range(19):
        cnt = 1
        winij.clear()
        for k in range(1, 19-j):
            if data[k][j+k] != 0 and data[k-1][j+k-1] == data[k][j+k]:
                cnt += 1
                winij.append([k, j+k])
            else:
                if cnt == 5:
                    win = data[k-1][j+k-1]
                    break
                cnt = 1
                winij.clear()
        else:
            if cnt == 5:
                win = data[k-1][j+k-1]
        if win != 0:
            break


data = [list(map(int, input().split())) for _ in range(19)]
data_t = list(zip(*data))
win = 0
winij = []

i = 18
for j in range(19):
    cnt = 1
    winij.clear()
    for k in range(1, 19-j):
        if data[i-k][j + k] != 0 and data[i-k + 1][j + k - 1] == data[i-k][j + k]:
            cnt += 1
            winij.append([i-k+2, j + k])
        else:
            if cnt == 5:
                win = data[i-k+1][j+k-1]
                break
            cnt = 1
            winij.clear()
    else:
        if cnt == 5:
            win = data[i-k+1][j+k-1]
    if win != 0:
        break


if win == 0:
    j = 0
    for i in range(19):
        cnt = 1
        winij.clear()
        for k in range(1, i+1):
            if data[i-k][j+k] != 0 and data[i-k+1][j+k-1] == data[i-k][j + k]:
                cnt += 1
                winij.append([i-k+2, j + k])
            else:
                if cnt == 5:
                    win = data[i-k+1][j+k-1]
                    break
                cnt = 1
                winij.clear()
        else:
            if cnt == 5:
                win = data[i-k+1][j+k-1]
        if win != 0:
            break

if win == 0:
    gase(data)

if win == 0:
    dea(data)

if win == 0:
    gase(data_t)
    if win != 0:
        winij[0] = winij[0][::-1]

if win == 0:
    dea(data_t)
    if win != 0:
        winij[0] = winij[0][::-1]

if win != 0:
    print(win)
    print(*winij[0])
else:
    print(win)
