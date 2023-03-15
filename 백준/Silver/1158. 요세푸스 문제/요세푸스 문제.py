import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(range(1, N+1))

result = []

cnt = 0
for i in data:
    cnt += 1
    if cnt == K:
        result.append(i)
        cnt = 0
    else:
        data.append(i)

print("<", end="")
print(*result, sep=", ", end="")
print(">")