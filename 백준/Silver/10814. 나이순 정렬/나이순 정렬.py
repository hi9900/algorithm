N = int(input())
lst = []
for _ in range(N):
    a, b = input().split()
    lst.append((_, a, b))

lst.sort(key=lambda x: (int(x[1]), x[0]))

for i, *j in lst:
    print(*j)