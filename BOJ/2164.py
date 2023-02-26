import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

card = range(1, N+1)
q = deque(card)

while len(q) != 1:
    q.popleft()
    q.rotate(-1)

print(q[0])