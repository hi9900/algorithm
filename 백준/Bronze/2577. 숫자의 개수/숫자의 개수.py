import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

multi = A * B * C

for i in range(10):
    print(str(multi).count(str(i)))
