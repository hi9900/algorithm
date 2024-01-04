import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

co = (1, 1, 2, 2, 2, 8)
ans = [0] * 6
for i in range(6):
    ans[i] = co[i] - arr[i]

print(*ans)
