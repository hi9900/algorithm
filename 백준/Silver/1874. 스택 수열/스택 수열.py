import sys
input = sys.stdin.readline

n = int(input())
num = 1
stack = [0]
result = []
for _ in range(n):
    want = int(input())
    while stack[-1] != want:
        stack.append(num)
        num += 1
        result.append("+")

        if num > n+1:
            result.clear()
            break

    if stack[-1] == want:
        stack.pop()
        result.append("-")

    if not result:
        break

if result:
    print(*result, sep="\n")
else:
    print("NO")