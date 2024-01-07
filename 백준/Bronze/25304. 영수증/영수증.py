import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
check = 0
for _ in range(N):
    a, b = map(int, input().split())
    check += a * b

print('Yes') if check == X else print('No')