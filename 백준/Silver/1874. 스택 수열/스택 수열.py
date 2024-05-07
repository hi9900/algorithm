n = int(input())
stack = []
ans = ''
i = 1

for _ in range(n):
    num = int(input())
    if i <= num:
        stack += list(range(i, num))
        ans += '+' * (num - i) + '+-'
        i = num + 1

    elif i > num:
        if not stack:
            print('NO')
            break
        while stack:
            x = stack.pop()
            ans += '-'

            if x == num:
                break
        else:
            print('NO')
            break

else:
    print('\n'.join(ans))