import sys
input = sys.stdin.readline

W, N = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: x[1],reverse=True)

result = 0
for i in range(N):
    w, p = data[i]
    if W - w >= 0:
        result += (w * p)
        W -= w

    else:
        result += (W * p)
        break

print(result)
