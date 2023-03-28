import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
if (a == b == c == 0 and f == 0) or (d == e == f == 0 and c == 0):
    x = 0
    y = 0

else:
    x = (c * e - b * f) // (a * e - b * d)
    y = (c * d - a * f) // (b * d - a * e)

print(int(x), int(y))