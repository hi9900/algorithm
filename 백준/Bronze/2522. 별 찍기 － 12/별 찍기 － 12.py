import sys
input = sys.stdin.readline

star = '*'
N = int(input())

for i in range(1, 2*N):
    if i > N:
        i = N - (i-N)
    print(f'{i * star:>{N}}')
    