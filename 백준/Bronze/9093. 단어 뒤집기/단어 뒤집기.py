import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = list(input().split())

    for i in A:
        print(i[::-1], end=" ")

    print()
