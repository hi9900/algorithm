import sys
input = sys.stdin.readline

T = int(input())

data0 = [0] * 41
data1 = [0] * 41

for i in range(41):
    if i == 0:
        data0[i] = 1
        data1[i] = 0
    elif i == 1:
        data0[i] = 0
        data1[i] = 1
    else:
        data0[i] = data0[i - 2] + data0[i - 1]
        data1[i] = data1[i - 2] + data1[i - 1]

for _ in range(T):
    N = int(input())
    print(data0[N], data1[N])