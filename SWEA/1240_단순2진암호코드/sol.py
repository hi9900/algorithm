import sys
sys.stdin = open("input.txt")


def findPasswordEnd(N, M):
    for i in range(N):
        for j in range(M-1, -1, -1):
            if data[i][j] == "1":
                return i, j


password = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
    }

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(input() for _ in range(N))
    ei, ej = findPasswordEnd(N, M)
    # print(data[ei][ej])
    code = []
    for i in range(ej-56+7, ej+1, 7):
        code.append(password[data[ei][i-6:i+1]])
    # print(code)
    odd = 0
    even = 0
    for i in range(8):
        # 실제 자리는 홀짝이 반대
        if i % 2:
            even += code[i]
        else:
            odd += code[i]

    if (odd * 3 + even) % 10 == 0:
        result = odd + even
    else:
        result = 0

    print(f"#{tc} {result}")