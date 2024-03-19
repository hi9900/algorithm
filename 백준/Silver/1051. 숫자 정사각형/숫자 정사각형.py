import sys
input = sys.stdin.readline


def solve(L):
    if L == 1:
        return 1
    for i in range(N-L+1):      # 0 ~ N-L
        for j in range(M-L+1):  # 0 ~ M-L
            a = data[i][j]
            b = data[i+L-1][j]
            c = data[i][j+L-1]
            d = data[i+L-1][j+L-1]

            if a == b == c == d:
                return L
    return solve(L-1)


N, M = map(int, input().split())
data = [input() for _ in range(N)]

# 정사각형 변의 길이
L = min(N, M)
print(solve(L) ** 2)