from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque(range(1, N+1))

result = []
while q:
    q.rotate(-K+1)
    result.append(str(q.popleft()))

print(f'<{", ".join(result)}>')