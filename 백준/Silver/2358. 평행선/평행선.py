import sys
input = sys.stdin.readline

N = int(input())
cnt_x = {}
cnt_y = {}

ans = 0

for _ in range(N):
    x, y = map(int, input().split(" "))
    cnt_x[x] = cnt_x.get(x, 0) + 1
    cnt_y[y] = cnt_y.get(y, 0) + 1


# 두 개 이상 점이 있는 x = c, y = c 의 개수 합
ans += sum(1 for v in cnt_x.values() if v >= 2)
ans += sum(1 for v in cnt_y.values() if v >= 2)

print(ans)
