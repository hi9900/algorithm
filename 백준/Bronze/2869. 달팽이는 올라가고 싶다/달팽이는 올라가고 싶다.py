import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    if (V-A) % (A-B):
        print((V-A) // (A-B) + 2)
    else:
        print((V-A) // (A-B) + 1)
