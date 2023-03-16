import sys
input = sys.stdin.readline

N = int(input())
building = []
v = 0
for _ in range(N):
    height = int(input())

    if building:
        while building[-1] <= height:
            building.pop()

            if not building:
                break
        else:
            v += len(building)

    building.append(height)

print(v)