N = int(input())

arr = [0] * N
for _ in range(N):
    arr[_] = int(input())

arr.sort(reverse=True)
print(*arr)