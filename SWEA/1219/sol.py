import sys
sys.stdin = open("input.txt")

T = 10
for _ in range(1, T+1):
    tc, N = map(int, input().split())
    data = list(map(int, input().split()))

    line = [[] for _ in range(99)]
    for i in range(N):
        line[data[i*2]].append(data[i*2+1])

    visited = [0] * 100
    stack = [0]
    result = 0

    while stack:
        now = stack[-1]
        if now == 99:
            result = 1
            break

        visited[now] = 1

        for node in line[now]:
            if visited[node] == 0:
                stack.append(node)
                break
        else:
            stack.pop()

    print(f"#{tc} {result}")
