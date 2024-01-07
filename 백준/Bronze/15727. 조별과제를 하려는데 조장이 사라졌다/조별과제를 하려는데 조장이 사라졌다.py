import sys
input = sys.stdin.readline

L = int(input())

# 1분에 1 ~ 5

# 1. 5보다 크면, 5만큼 이동한다.
# 2. 5보다 같거나 작으면, 찾을 수 있다.

A, B = divmod(L, 5)
if B == 0:
    print(A)
else:
    print(A + 1)


