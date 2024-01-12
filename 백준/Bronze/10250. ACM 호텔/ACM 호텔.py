import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 호텔의 층, 각 층의 방, N번째 손님
    H, W, N = map(int, input().split())

    """
    yxx / yyxx 호일때, x가 작은 호실
    x가 같다면, y가 작은 호실

    101 ~ H01 -> 102 ~ H02 -> ...
    """

    # 층수 y, 거리 x+1
    x, y = divmod(N, H)
    if y == 0:
        y = H
        x -= 1
    print(f'{y}{x+1:02d}')

