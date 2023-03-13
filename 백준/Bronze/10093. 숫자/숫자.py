import sys
input = sys.stdin.readline

A, B = map(int, input().split())
if B < A:
    A, B = B, A

mid = list(range(A+1, B))
print(len(mid))
print(*mid)