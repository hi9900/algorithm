import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num, *data = input().split()
    num = float(num)
    for i in data:
        if i == "@":
            num *= 3
        elif i == "%":
            num += 5
        elif i == "#":
            num -= 7

    print(f"{num:.2f}")