# https://www.acmicpc.net/problem/13300
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = {}
for i in range(N):
    a = tuple(map(int, input().split()))
    data[a] = data.get(a, 0) + 1
    # data.append(tuple(map(int, input().split())))

# print(data)
cnt = 0
for v in data.values():
    if v > K:
        if v % K:
            cnt += v // K + 1
        else:
            cnt += v // K

    elif v <= K:
        cnt += 1
print(cnt)