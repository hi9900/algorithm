import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    # i부터 j까지 뒤집기

    arr[i:j+1] = arr[j:i-1:-1]
print(*arr[1:])