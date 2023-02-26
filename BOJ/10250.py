import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 호텔층, 한층 당 방수, 몇번째손님
    H, W, N = map(int, input().split())

    if N <= H:
        floor = N
        ho = 1
        print(floor * 100 + ho)
    else:
        ho, floor = divmod(N, H)
        ho += 1
        if floor == 0:
            floor = H
            ho -= 1
        print(floor*100 + ho)

