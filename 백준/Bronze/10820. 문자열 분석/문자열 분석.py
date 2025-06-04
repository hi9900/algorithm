import sys
input = sys.stdin.readline

while 1:
    str = input()
    ans = [0, 0, 0, 0] # 소문자, 대문자, 숫자, 공백

    if not str:
        break

    for s in str:
        if s in 'abcdefghijklmnopqrstuvwxyz':
            ans[0] += 1
            continue

        if s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ans[1] += 1
            continue

        if s == ' ':
            ans[3] += 1
            continue

        if s in '0123456789':
            ans[2] += 1
            continue

    print(*ans)
