N, M = map(int, input().split())
money = [0] * N
for _ in range(N):
    money[_] = int(input())
money.sort()

result = [0] + [10001] * M

for i in money:
    for j in range(i, M+1):
        if result[j-i] != 10_001:
            result[j] = min(result[j-i] + 1, result[j])

print(-1 if result[M] == 10_001 else result[M])
