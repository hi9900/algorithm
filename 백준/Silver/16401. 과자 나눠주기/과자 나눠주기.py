import sys
input = sys.stdin.readline

m, n = map(int, input().split())
l = list(map(int, input().split()))

s, e = 1, max(l)
ans = 0

while 1:
    if s > e:
        break

    mid = (s + e) // 2
    pieces = 0
    for i in l:
        pieces += i // mid

    if pieces >= m:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
