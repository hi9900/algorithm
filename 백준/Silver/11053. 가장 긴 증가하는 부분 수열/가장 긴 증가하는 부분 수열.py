import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

num = [1] * N
for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if A[i] < A[j]:
            num[i] = max(num[i], 1+num[j])

print(max(num))