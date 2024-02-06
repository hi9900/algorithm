import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        # 점과의 관계
        d1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** (1/2)
        d2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** (1/2)

        # 거리가 r보다 작으면, 원의 내부
        # print(d1 < r)
        # print(d2 < r)

        # 두 점이 모두 한 원의 내부이면, 패스
        if d1 < r and d2 < r:
            pass
        # 한 점만 내부이면, 진입/이탈 +1
        elif d1 < r or d2 < r:
            cnt += 1

    print(cnt)