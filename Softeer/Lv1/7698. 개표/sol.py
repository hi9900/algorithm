import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 1개 |
    # 5개 ++++
    
    n = int(input())
    a, b = divmod(n, 5)
    print('++++ ' * a, end="")
    print('|' * b)