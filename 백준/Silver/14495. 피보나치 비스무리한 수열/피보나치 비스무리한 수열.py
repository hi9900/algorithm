import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * 117
arr[1] = arr[2] = arr[3] = 1

for i in range(4, 117):
    arr[i] = arr[i-1] + arr[i-3]

print(arr[N])
