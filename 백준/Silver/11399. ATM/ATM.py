import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
now = 0
result = 0

for i in arr:
    now += i
    result += now

print(result)