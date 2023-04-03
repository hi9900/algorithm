import sys
input = sys.stdin.readline

N = int(input())
enter = set()

for _ in range(N):
    name, check = input().split()
    if check == "enter":
        enter.add(name)
    elif check == "leave":
        if name in enter:
            enter.remove(name)
enter = sorted(enter, reverse=True)
print(*enter, sep="\n")