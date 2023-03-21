import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
data = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        data.append(i)
if data:
    print(sum(data))
    print(data[0])
else:
    print(-1)