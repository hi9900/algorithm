N, M = map(int, input().split())
balls = list(map(int, input().split()))

result = 0

for i in range(N):
    a = balls[i]
    for j in range(i + 1, N):
        if a != balls[j]:
            result += 1

print(result)
