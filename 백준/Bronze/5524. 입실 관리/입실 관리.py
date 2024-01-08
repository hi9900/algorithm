"""
65 ~ 90 대문자
97 ~ 122 소문자

대문자 -> 소문자 = +32
"""
N = int(input())
for _ in range(N):
    name = input()
    for c in name:
        if ord(c) <= 90:
            print(chr(ord(c) + 32), end="")
        else:
            print(c, end="")
    print()