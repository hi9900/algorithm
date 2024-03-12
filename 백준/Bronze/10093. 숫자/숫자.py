import sys
input = sys.stdin.readline

A, B = map(int, input().split())
if A > B:
    A, B = B, A
result = list(range(A+1, B))
if result:
    print(len(result))
    print(*result)
else:
    print(0)
