import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

data = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

v = [0] * (N+1)
p = [1]

while p:
    virus = p.pop()
    v[virus] = 1
    for i in data[virus]:
        if v[i] == 0:
            p.append(i)

print(v.count(1) - 1)
