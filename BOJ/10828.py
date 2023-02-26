import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    data = input().split()
    if "push" in data:
        stack.append(int(data[-1]))
    elif "pop" in data:
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif "size" in data:
        print(len(stack))
    elif "empty" in data:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in data:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
# print(stack)