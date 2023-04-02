import sys
sys.stdin = open("input.txt")

# 16진수 1자리 -> 2진수 4자리

T = int(input())
for tc in range(1, T+1):
    N, N16 = input().split()
    result = ""
    for i in N16:
        # 16 -> 10
        N10 = int(i, 16)

        # 10 -> 2
        result += (bin(N10)[2:]).zfill(4)

    print(f"#{tc} {result}")
