import sys
input = sys.stdin.readline

# 0.25, 0.10, 0.05, 0.01

T = int(input())
for _ in range(T):
    C = int(input())

    a, C = divmod(C, 25)
    b, C = divmod(C, 10)
    c, C = divmod(C, 5)
    d, C = divmod(C, 1)

    print(a, b, c, d)
    