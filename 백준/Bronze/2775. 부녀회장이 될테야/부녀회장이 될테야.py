import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    data = [x for x in range(N+1)]
    for i in range(K):
        for j in range(1, N+1):
            data[j] = data[j-1] + data[j]
    print(data[-1])
