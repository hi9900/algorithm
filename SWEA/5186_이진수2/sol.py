import sys
sys.stdin = open("input.txt")

# 0.xxx(10) -> 2
T = int(input())
for tc in range(1, T+1):
    N = float(input())

    result = ""
    # 소수부에 2를 곱해 그 결과가 1로 떨어지거나 똑같은 소수점이 나올 때 까지
    while N:
        N *= 2
        if N >= 1:
            N -= 1
            result += "1"
        else:
            result += "0"

    if len(result) >= 13:
        result = "overflow"
    print(f"#{tc} {result}")
