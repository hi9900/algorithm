import sys
input = sys.stdin.readline

N = int(input())

star = '*'
for i in range(1, 2*N, 2):
    print(f'{star * i:^{2*N}}'.rstrip())
