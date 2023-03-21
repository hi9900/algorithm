import sys
input = sys.stdin.readline

data = [[] for _ in range(15)]
for _ in range(5):
    char = input().rstrip()
    for i in range(len(char)):
        data[i].append(char[i])

for p in data:
    print(*p, sep="", end="")
