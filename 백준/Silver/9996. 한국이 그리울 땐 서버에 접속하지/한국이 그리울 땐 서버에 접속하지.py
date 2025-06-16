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

    if file.startswith(prefix) and file.endswith(suffix):
        print("DA")
        continue

    print("NE")
