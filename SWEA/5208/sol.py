import sys
sys.stdin = open("input.txt")


def bus(i, e, b, c):
    global cnt
    if c >= cnt:
        return

    # if i == e:
    #     cnt = min(c, cnt)
    #     return

    for j in range(i + 1, i + b + 1):
        if j == e:
            cnt = min(c, cnt)
            return
        bus(j, e, M[j], c+1)


T = int(input())
for tc in range(1, T+1):
    N, *M = map(int, input().split())
    cnt = N
    bus(0, N-1, M[0], 0)

    print(f"#{tc} {cnt}")
