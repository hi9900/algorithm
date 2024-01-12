import sys
input = sys.stdin.readline

x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()


if x.count(x[0]) == 1:
    rx = x[0]
else:
    rx = x[-1]
if y.count(y[0]) == 1:
    ry = y[0]
else:
    ry = y[-1]

print(rx, ry)