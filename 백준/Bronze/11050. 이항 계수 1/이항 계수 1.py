import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 6C4 -> 6C2
if N-K < K:
    K = N - K

result1 = 1
result2 = 1
while 1:
    if K == 0:
        break

    result1 *= N
    result2 *= K
    N -= 1
    K -= 1

print(result1 // result2)
