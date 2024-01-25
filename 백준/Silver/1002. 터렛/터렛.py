import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dis = ((x2-x1)**2 + (y2-y1)**2) ** (0.5)
    # print(dis, r1+r2)
    
    # 원점 동일
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    # 내부
    elif dis < max(r1, r2):
        # 내접
        if dis == max(r1, r2) - min(r1, r2):
            print(1)
        elif dis > max(r1, r2) - min(r1, r2):
            print(2)
        else:
            print(0)

    # 외부
    else:
        if dis == r1+r2:
            print(1)
        elif dis > r1+r2:
            print(0)
        else:
            print(2)
