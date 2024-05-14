import sys
input = sys.stdin.readline

M = int(input())

s = set()
for _ in range(M):
    a, *n = input().split()

    if a == 'add':
        s.add(int(n[0]))

    if a == 'remove':
        if int(n[0]) in s:
            s.remove(int(n[0]))

    if a == 'check':
        if int(n[0]) in s:
            print(1)
        else:
            print(0)

    if a == 'toggle':
        if int(n[0]) in s:
            s.remove(int(n[0]))
        else:
            s.add(int(n[0]))

    if a == 'all':
        s = set(range(1, 20+1))

    if a == 'empty':
        s = set()
