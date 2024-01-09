import sys
input = sys.stdin.readline

while 1:
    M, F = map(int, input().split())
    if M + F == 0:
        break

    print(M + F)
    