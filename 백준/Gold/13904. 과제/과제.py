N = int(input())
data = []
for _ in range(N):
    d, w = map(int, input().split())
    data.append((d, w))

data.sort(key=lambda x: (x[0], x[1]))

can = []
ans = 0
for i in range(N, 0, -1):
    # i 날짜에 수행할 수 있는 과제
    while data and data[-1][0] >= i:
        can.append(data.pop())
    # 중 점수가 큰 값을 수행한다.
    can.sort(key=lambda x: x[1])
    if can:
        ans += can.pop()[1]

print(ans)
