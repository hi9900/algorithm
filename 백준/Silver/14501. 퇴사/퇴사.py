import sys
input = sys.stdin.readline


def sol2(day, remain, money):
    global result
    if day == N:
        if remain > 0:
            return 0
        return money
    result = sol2(day+1, remain-1, money)
    if remain <= 0:
        result = max(result, sol2(day+1, days[day]-1, money+pays[day]))
    return result


N = int(input())
days = [0] * N
pays = [0] * N
for _ in range(N):
    T, P = map(int, input().split())
    days[_] = T
    pays[_] = P

result = 0
sol2(0, 0, 0)
print(result)


