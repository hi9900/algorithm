import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a, b = divmod(n, m)
print(a, b, sep="\n")