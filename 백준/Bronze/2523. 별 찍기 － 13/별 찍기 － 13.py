import sys
input = sys.stdin.readline

n = int(input())
star = '*'
for i in range(1, 2*n):
    if i > n:
        i = n - abs(i-n)
    print(i*star)
