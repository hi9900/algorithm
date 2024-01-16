import sys
input = sys.stdin.readline
"""
a == 1: 1
a == 2: 2, 4, 8, 16, 32, ...
a == 3: 3, 9, 7, 1, 3, ...
a == 4: 4, 6, 4, 6, ...
a == 5: 5, 5, 5, 5, ...
a == 6: 6, 6, 6, 6, ...
a == 7: 7, 9, 3, 1, ...
a == 8: 8, 4, 2, 6, 
a == 9: 9, 1, 9, 1, 
a == 10: 10, 10, 10, 10

b -> b%4, 1 2 3 0
"""

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    if b % 4 == 0:
        b1 = 4
    else:
        b1 = b % 4

    if a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 10:
        print(10)
    else:
        print((a**b1) % 10) if (a**b1) % 10 != 0 else print(10)
