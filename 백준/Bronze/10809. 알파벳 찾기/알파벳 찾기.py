import sys
input = sys.stdin.readline

S = input().rstrip()

for i in range(97, 123):
    print(S.find(chr(i)), end=" ")
    