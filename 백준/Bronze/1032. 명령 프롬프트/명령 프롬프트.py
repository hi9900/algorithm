import sys
input = sys.stdin.readline

N = int(input())
files = []
for _ in range(N):
    files.append(input().rstrip())

pattern = []
for i in range(len(files[0])):
    key = files[0][i]
    for j in range(1, N):
        if files[j][i] != key:
            pattern.append('?')
            break
    else:
        pattern.append(key)

print(*pattern, sep="")
