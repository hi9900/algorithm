import sys
input = sys.stdin.readline


def lotto(d, i, n):
    if d == n:
        print(*v)
        return

    for j in range(i, k):
        v[d] = S[j]
        lotto(d+1, j+1, n)


k = 1
while k != 0:
    k, *S = map(int, input().split())
    v = [0] * 6
    lotto(0, 0, 6)
    print()