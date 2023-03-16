import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    word = input().split()
    for re in word:
        print(re[::-1], end=" ")
    print()
