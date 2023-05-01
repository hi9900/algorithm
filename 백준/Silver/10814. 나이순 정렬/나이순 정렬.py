import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    (age, name) = input().split()
    lst.append((_, int(age), name))

lst = sorted(lst, key=lambda x: (x[1], x[0]))

for _ in range(N):
    print(*lst[_][1:])