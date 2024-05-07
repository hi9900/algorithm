N = int(input())
data = []

for _ in range(N):
    x, y = map(int, input().split())
    data.append((x, y))

ans = [1] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            ans[i] += 1

print(*ans)