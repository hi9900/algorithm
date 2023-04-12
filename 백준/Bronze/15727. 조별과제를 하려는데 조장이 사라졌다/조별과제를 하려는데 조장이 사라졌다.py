import sys
input = sys.stdin.readline

L = int(input())
t = 1

while L > 5:
    t += 1
    L -= 5

print(t)
