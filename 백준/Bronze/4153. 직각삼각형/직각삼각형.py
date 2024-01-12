import sys
input = sys.stdin.readline

while 1:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break

    # a2 + b2 = c2
    lst.sort()
    if lst[-1] ** 2 == lst[0] ** 2 + lst[1] ** 2:
        print('right')
    else:
        print('wrong')
