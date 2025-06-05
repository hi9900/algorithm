import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    f = input().strip()
    n = 0

    if '0' in f:
        f = f.split('0')
        n = 0
    elif '1' in f:
        f = f.split('1')
        n = 1

    if len(f[1]) > 0:   # 1
        if len(f[0]) % 2 == 0:
            print(1)
        else:
            print(0)
    else:   # n
        if len(f[0]) % 2 == 0:
            print(n)
        else:
            print(0 if n == 1 else 1)
