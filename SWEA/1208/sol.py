import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    # 상자의 높이를 담을 리스트, H[i] = i높이의 상자 개수
    H = [0] * 101
    for box in data:
        H[box] += 1

    dump = 1
    while dump <= N:
        for m in range(1, 101):
            if H[m]:
                H[m] -= 1
                H[m+1] += 1
                if H[m] != 0:
                    min_h = m
                else:
                    min_h = m+1
                break
        for M in range(100, 0, -1):
            if H[M]:
                H[M] -= 1
                H[M-1] += 1
                if H[M] != 0:
                    max_h = M
                else:
                    max_h = M-1
                break
        dump += 1

        if max_h - min_h == 1:
            break

    print(f"#{tc} {max_h - min_h}")
