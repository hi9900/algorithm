import sys
input = sys.stdin.readline

N = int(input())

ans, N = divmod(N, 5)
while ans >= 0:
    if N == 0:
        break

    if N % 2 == 0:
        ans += N // 2
        break

    else:
        ans -= 1
        N += 5

print(ans)

