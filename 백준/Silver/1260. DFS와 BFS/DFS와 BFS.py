import sys
input = sys.stdin.readline
from collections import deque

stack = []
v = set()
def DFS(start):
    stack.append(start)
    v.add(start)

    while stack:
        c = stack.pop()
        print(c, end=" ")
        for i in lst[c]:
            if i not in v:
                DFS(i)


def BFS(start):
    queue = deque()
    queue.append(start)
    v_b = set()
    v_b.add(start)
    while queue:
        c = queue.popleft()
        print(c, end=" ")
        for i in lst[c]:
            if i not in v_b:
                queue.append(i)
                v_b.add(i)


N, M, V = map(int,input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    lst[v1].append(v2)
    lst[v2].append(v1)
    lst[v1].sort()
    lst[v2].sort()

# print(lst)
DFS(V)
print()
BFS(V)