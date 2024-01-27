import sys
input = sys.stdin.readline

# 팩토리얼
data = [0] * 31
data[0] = 1
data[1] = 1
for i in range(2, 31):
    data[i] = data[i-1] * i

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # M C N = M! / ((M-N)! * N!)
    print(data[M] // (data[M-N] * data[N]))

