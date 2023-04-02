import sys
sys.stdin = open("input.txt")


password = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}


T = int(input())
for tc in range(1, T+1):
    N16 = input()
    code = ""
    ei = 0
    for i in N16:
        code += bin(int(i, 16))[2:].zfill(4)

    for i in range(len(code)-1, -1, -1):
        if code[i] == "1":
            ei = i
            break
    result = []
    for i in range(ei, -1, -6):
        if i-5 < 0:
            continue
        # print(password[code[i - 5:i + 1]])
        result.append(password[code[i-5:i+1]])

    print(*result[::-1])