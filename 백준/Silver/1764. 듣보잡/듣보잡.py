import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nohear = set()
nosee = set()

for _ in range(N):
    nohear.add(input().rstrip())

for _ in range(M):
    nosee.add(input().rstrip())

nohs = sorted(nohear & nosee)
print(len(nohs))
print(*nohs, sep="\n")