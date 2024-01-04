import sys
input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N*i}')