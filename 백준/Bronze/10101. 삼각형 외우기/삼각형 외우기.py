import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180:
    angles = set()
    angles.update([A, B, C])
    if len(angles) == 1:
        print('Equilateral')
    elif len(angles) == 2:
        print('Isosceles')
    elif len(angles) == 3:
        print('Scalene')
else:
    print('Error')
