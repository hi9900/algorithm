import sys
sys.stdin = open("input.txt")

# 16진수 문자를 앞에서부터 7bit 씩 묶어 십진수로 변환
T = int(input())
for tc in range(1, T+1):
    N16 = input()

    N2 = ""
    for i in N16:
        N2 += bin(int(i, 16))[2:].zfill(4)

    for i in range(0, len(N2), 7):
        print(int(N2[i:i+7], 2), end=" ")

    print()