data = 'aeiouAEIOU'

while 1:
    desc = input()

    if desc == '#':
        break

    cnt = 0
    for c in desc:
        if c in data:
            cnt += 1

    print(cnt)
    