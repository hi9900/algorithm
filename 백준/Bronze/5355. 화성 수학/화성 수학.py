for _ in range(int(input())):
    n, *arr = input().split()

    result = float(n)
    for a in arr:
        if a == '@':
            result *= 3
        elif a == '%':
            result += 5
        elif a == '#':
            result -= 7

    print(f'{result:.2f}')
