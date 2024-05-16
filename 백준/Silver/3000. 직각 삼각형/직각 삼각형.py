N = int(input())
dots = []
xCount = [0] * 100_001
yCount = [0] * 100_001

for _ in range(N):
    X, Y = map(int, input().split())
    xCount[X] += 1
    yCount[Y] += 1

    dots.append((X, Y))

result = 0
for dotX, dotY in dots:
    result += (xCount[dotX] - 1) * (yCount[dotY] - 1)

print(result)