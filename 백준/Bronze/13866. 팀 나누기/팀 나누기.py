import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

# 최대 + 최소 / 남은 두명
A = max(lst) + min(lst)
B = sum(lst) - A

print(abs(A - B))