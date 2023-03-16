import sys
input = sys.stdin.readline

N = int(input())
NGE = list(map(int, input().split()))
result = [-1] * N
stack = [NGE.pop()]
for i in range(N-2, -1, -1):
    while stack:
        if NGE[-1] < stack[-1]:
            result[i] = stack[-1]
            break
        else:
            stack.pop()

    stack.append(NGE.pop())

print(*result)