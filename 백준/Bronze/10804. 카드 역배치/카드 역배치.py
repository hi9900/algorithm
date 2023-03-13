import sys
input = sys.stdin.readline

data = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    mid = (b-a+1)//2
    
    for i in range(mid):
        data[a+i], data[b-i] = data[b-i], data[a+i]

print(*data[1:])
