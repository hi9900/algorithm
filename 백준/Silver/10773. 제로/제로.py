import sys
input = sys.stdin.readline

K = int(input())
data = []
for _ in range(K):
    num = int(input())
    if num == 0:
        data.pop()
    else:
        data.append(num)

print(sum(data))