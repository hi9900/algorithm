import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    result = 0
    data = []
    for _ in range(N):
        S, L = input().split()
        data.append([S, int(L)])
    data.sort(key=lambda x: x[1])
    print(data[-1][0])
