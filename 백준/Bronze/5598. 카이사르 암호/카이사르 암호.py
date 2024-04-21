C = input()

for c in C:
    num = ord(c) - 3
    if num < 65:
        num = 90 - (65 - num - 1)
    print(chr(num), end='')