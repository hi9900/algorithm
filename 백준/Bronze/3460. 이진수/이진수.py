T = int(input())

for _ in range(T):
    n = int(input())

    # n을 이진수로
    bin_n = bin(n)[2:]
    # 1의 위치
    L = len(bin_n)
    result = []
    for i in range(L-1, -1, -1):
        if bin_n[i] == '1':
            result.append(L - i - 1)
    print(*result)