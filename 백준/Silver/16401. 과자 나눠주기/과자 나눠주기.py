import sys
input = sys.stdin.readline

M, N = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
ans = 0

low = 1
high = max(arr)

while low <= high:
    mid = (low + high) // 2

    count = 0
    for a in arr:
        count += a // mid

    if count >= M:
        ans = max(ans, mid)
        low = mid + 1
    else:
        high = mid - 1

print(ans)
