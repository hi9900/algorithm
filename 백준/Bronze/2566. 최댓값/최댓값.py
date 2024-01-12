import sys
input = sys.stdin.readline

# 최댓값과 그 위치
result = -1
x, y = 0, 0

for i in range(9):
    lst = list(map(int, input().split()))

    for j in range(9):
        if lst[j] > result:
            result = lst[j]
            x, y = i+1, j+1

print(result)
print(x, y)