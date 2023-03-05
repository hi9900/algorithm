import sys
input = sys.stdin.readline

data = []
for _ in range(9):
    data.append(int(input()))

data.sort()
result = 0
result = sum(data)
for i in range(9):
    for j in range(i+1, 9):
        if result - (data[i] + data[j]) == 100:
            nonan = (j, i)
            break
# print(sum(data[:8]))
for no in nonan:
    del data[no]

print(*data)