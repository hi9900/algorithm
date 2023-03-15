import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    data = list(input().rstrip())
    data_f = []
    data_b = []

    for i in data:
        if i == "<":
            if data_f:
                data_b.append(data_f.pop())
        elif i == ">":
            if data_b:
                data_f.append(data_b.pop())
        elif i == "-":
            if data_f:
                data_f.pop()
        else:
            data_f.append(i)
    print(*data_f, *data_b[::-1], sep="")