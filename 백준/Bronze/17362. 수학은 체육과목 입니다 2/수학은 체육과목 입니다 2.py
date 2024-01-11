import sys
input = sys.stdin.readline

n = int(input())
"""
1 2 3 4 5
9 8 7 6
  10 11 12 13
17 16 15 14  -> +8
  18 19 20 21
25 24 23 22  -> +8

1 0,2 7,3 6,4 5

1 ~ 5 는 하나씩
"""
a, b = divmod(n, 8)

if b == 1:
    print(1)
elif b == 0 or b == 2:
    print(2)
elif b == 3 or b == 7:
    print(3)
elif b == 4 or b == 6:
    print(4)
elif b == 5:
    print(5)
    