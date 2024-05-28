import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = dict()

for _ in range(N):
    site, password = input().split()
    a[site] = password

for _ in range(M):
    site = input().rstrip()
    print(a[site])