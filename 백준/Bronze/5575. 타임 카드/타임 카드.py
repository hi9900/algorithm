import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(3)]

for i in data:
    if i[5] < i[2]:
        i[4] -= 1
        i[5] += 60
    data_s = i[5] - i[2]

    if i[4] < i[1]:
        i[3] -= 1
        i[4] += 60
    data_m = i[4] - i[1]

    data_h = i[3] - i[0]

    print(data_h, data_m, data_s)
