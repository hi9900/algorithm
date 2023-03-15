import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

stack = [0]
result = [0] * N

for i in range(N):
    while stack:
        if data[stack[-1]] > data[i]:
            result[i] = stack[-1] + 1
            break
        else:
            stack.pop()
    stack.append(i)

print(*result)