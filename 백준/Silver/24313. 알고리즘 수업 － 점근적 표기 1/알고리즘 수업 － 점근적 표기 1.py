import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())
n = int(input())

if a <= c:
    if a == c:
        if b <= 0:
            print(1)
        else:
            print(0)
    elif n >= b/(c-a):
        print(1)
    else:
        print(0)
else:
    print(0)