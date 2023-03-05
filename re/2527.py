import sys
input = sys.stdin.readline

for _ in range(4):
    result = 0
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if (x1, y1, p1, q1) == (x2, y2, p2, q2):
        print("a")
        continue

    one = [(x1, y1), (p1, y1), (p1, q1), (x1, q1)]
    two = [(x2, y2), (p2, y2), (p2, q2), (x2, q2)]

    for xo, yo in one:
        if x2 < xo < p2 and y2 < yo < q2:
            print("a")
            result = 1
            break
        if (xo, yo) in two:
            print("c")
            result = 1
            break
    if result:
        continue

    if x2 < x1 < p2 and x2 < p1 < p2 and y1 < y2 and q1 > q2:
        print("a")
        continue

    for xt, yt in two:
        if x1 < xt < p1 and y1 < yt < q1:
            print("a")
            result = 1
            break
        if (xt, yt) in one:
            print("c")
            result = 1
    if result:
        continue

    if x1 < x2 < p1 and x1 < p2 < p1 and y2 < y1 and q2 > q1:
        print("a")
        continue

    if x1 == p2 and (y2 <= y1 <= q2 or y1 <= p2 <= q1)\
        or p1 == x2 and (y2 <= q1 <= q2 or y1 <= y2 <= q1)\
            or y1 == q2 and (x2 <= x1 <= p2 or x1 <= p2 <= p1)\
            or q1 == y2 and (x2 <= p1 <= p2 or x1 <= x2 <= p1):
        print("b")
        continue

    else:
        print("d")

