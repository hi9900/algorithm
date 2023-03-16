import sys
input = sys.stdin.readline

word = input()
stack = []
tag = []
result = []

tags = 0
for c in word:
    tags += 1

    if c == " " and "<" not in stack:
        while stack:
            result.append(stack.pop())
        result.append(c)
    elif c == "<":
        tags = 0
        while stack:
            result.append(stack.pop())
        stack.append(c)

    elif c == ">":
        stack.append(c)
        result.append(stack[:])
        stack.clear()
    elif c == "\n":
        if "<" in stack:
            result.append(stack[:])
        else:
            result.append(stack[::-1])
        stack.clear()
    else:
        stack.append(c)

for r in result:
    print(*r, sep="", end="")