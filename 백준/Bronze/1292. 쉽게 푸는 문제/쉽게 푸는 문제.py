import sys
input = sys.stdin.readline

A, B = map(int, input().split())

data = []
num = 1
cnt = num

while 1:
    if len(data) >= B:
        break

    for i in range(cnt):
        data.append(num)

        if len(data) >= B:
            break
    else:
        num += 1
        cnt = num

print(sum(data[A-1:B]))