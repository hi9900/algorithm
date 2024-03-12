import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cost, result = 0, ''

    for _ in range(int(input())):
        c, name = input().split()
        if cost < int(c):
            cost = int(c)
            result = name
    print(result)
