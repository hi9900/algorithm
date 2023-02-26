import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    data = input().split()
    if "push_front" in data:
        q.appendleft(int(data[-1]))
    elif "push_back" in data:
        q.append(int(data[-1]))
    elif "pop_front" in data:
        if len(q) >= 1:
            print(q.popleft())
        else:
            print(-1)
    elif "pop_back" in data:
        if len(q) >= 1:
            print(q.pop())
        else:
            print(-1)
    elif "size" in data:
        print(len(q))
    elif "empty" in data:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif "front" in data:
        if len(q) >= 1:
            print(q[0])
        else:
            print(-1)
    elif "back" in data:
        if len(q) >= 1:
            print(q[-1])
        else:
            print(-1)
