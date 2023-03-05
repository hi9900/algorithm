import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

arr = [1]
for i in range(1, N):
    arr.insert(len(arr)-data[i], i+1)

print(*arr)