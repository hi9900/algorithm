import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
Y, M = 0, 0

for time in arr:
    # 30초마다 10원
    x1, y1 = divmod(time, 30)
    Y += (x1 + 1) * 10
    # 60초마다 15원
    x2, y2 = divmod(time, 60)
    M += (x2 + 1) * 15

print('M' if Y > M else 'Y' if Y < M else 'Y M', end=" ")
print(min(Y, M))
