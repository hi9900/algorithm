import sys
input = sys.stdin.readline

N = int(input())
F = list(map(int, input().split()))

F.sort()
print(max(F[0] * F[1], F[-1] * F[-2]))
