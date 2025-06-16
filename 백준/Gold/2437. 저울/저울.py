import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()

res = 1
for w in arr:
    if w > res:
        break
    res += w

print(res)