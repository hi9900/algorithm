import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    a, *b = input().split()
    if a == 'push_front':
        q.appendleft(int(b[0]))
    elif a == 'push_back':
        q.append(int(b[0]))
    elif a == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif a == 'pop_back':
        print(q.pop()) if q else print(-1)
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        print(0) if q else print(1)
    elif a == 'front':
        print(q[0]) if q else print(-1)
    elif a == 'back':
        print(q[-1]) if q else print(-1)
