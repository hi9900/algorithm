import sys
input = sys.stdin.readline

N = int(input())
[prefix, suffix] = input().strip().split('*')
p = len(prefix)
s = len(suffix)

for _ in range(N):
    file = input().strip()

    if len(file) < p + s:
        print("NE")
        continue

    if file[0:p] != prefix:
        print("NE")
        continue

    if file[-s:] != suffix:
        print("NE")
        continue

    print("DA")
