import sys
input = sys.stdin.readline

data = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    data.append((int(y), int(m), int(d), name))

# 나이 많은 순 정렬
data.sort(key=lambda x: (x[0], x[1], x[2]))
print(data[-1][-1])
print(data[0][-1])
