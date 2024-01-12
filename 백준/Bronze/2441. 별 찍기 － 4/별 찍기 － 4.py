import sys
input = sys.stdin.readline

N = int(input())
star = '*'
for i in range(N, 0, -1):
    print(f'{star * i:>{N}s}')