import sys
input = sys.stdin.readline


# push X: 정수 x를 스택에 넣음
def push(stack, x):
    stack.append(x)

# pop: 가장 위에 있는 정수를 빼고, 출력 / 정수가 없다면 -1
def pop(stack):
    if size(stack) == 0:
        return -1
    return stack.pop()

# size
def size(stack):
    return len(stack)

# empty
def empty(stack):
    if size(stack) == 0:
        return 1
    return 0

# top
def top(stack):
    if size(stack) == 0:
        return -1
    return stack[-1]


stack = []
N = int(input())
for _ in range(N):
    a = list(input().split())
    if a[0] == 'push':
        push(stack, a[1])
    elif a[0] == 'pop':
        print(pop(stack))
    elif a[0] == 'size':
        print(size(stack))
    elif a[0] == 'empty':
        print(empty(stack))
    elif a[0] == 'top':
        print(top(stack))
