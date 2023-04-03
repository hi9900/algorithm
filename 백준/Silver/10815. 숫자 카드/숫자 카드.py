import sys
input = sys.stdin.readline

N = int(input())
sang = set(map(int, input().split()))

M = int(input())
have = list(map(int, input().split()))
result = [0] * M

for i in range(M):
    if have[i] in sang:
        result[i] = 1

print(*result)