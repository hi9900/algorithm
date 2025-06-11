import sys
input = sys.stdin.readline

N = int(input())
good_count = 0
for _ in range(N):
    word = input().strip()
    stack = []

    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    else:
        if len(stack) == 0:
            good_count += 1

print(good_count)
