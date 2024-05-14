while 1:
    stack = []
    data = input()

    if data == '.':
        break

    for c in data:
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)

        elif c == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif c == ']':
            if not stack or stack.pop() != '[':
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')
