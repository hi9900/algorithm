import sys
input = sys.stdin.readline

data = {
    0: [1, 2, 3, 5, 6, 7],
    1: [3, 5],
    2: [2, 3, 4, 6, 7],
    3: [2, 3, 4, 5, 6],
    4: [1, 3, 4, 5],
    5: [1, 2, 4, 5, 6],
    6: [1, 2, 4, 5, 6, 7],
    7: [1, 2, 3, 5],
    8: [1, 2, 3, 4, 5, 6, 7],
    9: [1, 2, 3, 4, 5, 6],
}

T = int(input())
for _ in range(T):
    cnt = 0
    A, B =map(int, input().split())
    # 1의자리부터
    while 1:
        if A + B == 0:
            break
            
        A, a1 = divmod(A, 10)
        B, b1 = divmod(B, 10)

        if A == 0 and a1 == 0:
            a = set()
        else:
            a = set(data[a1])
        if B == 0 and b1 == 0:
            b = set()
        else:
            b = set(data[b1])
        
        cnt += len(a - b) + len(b - a)

    print(cnt)
