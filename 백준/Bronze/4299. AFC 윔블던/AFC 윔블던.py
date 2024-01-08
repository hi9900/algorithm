import sys
input = sys.stdin.readline

A, B = map(int, input().split())

'''
x > y

x + y = A
x - y = B

2x = A + B
x = (A + B) / 2

y = A - x
'''

if (A + B) % 2:
    print(-1)
else:
    x = (A + B) // 2
    y = A - x
    if y < 0:
        print(-1)
    else:
        print(x, A - x)
