import sys
input = sys.stdin.readline


A, B = 1, 1
while 1:
    A, B = map(int, input().split())
    if A+B == 0:
        break
    if A > B:
        print("Yes")
    else:
        print("No")