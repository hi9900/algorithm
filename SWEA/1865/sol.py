import sys
sys.stdin = open("input.txt")


def goodWork(i, N, per):
    global result
    if per <= result:
        return
    if i == N:
        result = max(per, result)
        return
    for j in range(N):
        if not c[j]:
            c[j] = 1
            goodWork(i+1, N, per*(P[i][j]/100))
            c[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    c = [0] * N
    result = 0

    goodWork(0, N, 1)
    print(f"#{tc} {result*100:6f}")

