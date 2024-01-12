import sys
input = sys.stdin.readline

N = int(input())

star = '*'
S = 2*N-1 
for i in range(S, 1, -2):
    print(f'{star * i:^{S}}'.rstrip())
for i in range(1, S+1, 2):
    print(f'{star * i:^{S}}'.rstrip())
