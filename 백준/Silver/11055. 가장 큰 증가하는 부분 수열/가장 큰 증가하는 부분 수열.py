import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

num = [A[i] for i in range(N)]

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if A[i] < A[j]:
            num[i] = max(num[i], A[i]+num[j])

print(max(num))