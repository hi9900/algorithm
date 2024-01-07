import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A, B = divmod(n, m)
print(A, B, sep="\n")