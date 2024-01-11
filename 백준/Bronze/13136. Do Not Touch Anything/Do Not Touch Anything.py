import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())

a, b = divmod(R, N)
c, d = divmod(C, N)

if b == 0:
    x = a
else:
    x = a + 1

if d == 0:
    y = c
else:
    y = c + 1

print(x * y)