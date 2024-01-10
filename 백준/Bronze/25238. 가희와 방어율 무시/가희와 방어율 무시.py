import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = a * (b / 100)
print(0) if a - ans >= 100 else print(1)
