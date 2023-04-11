import sys
input = sys.stdin.readline

while 1:
    data = input().rstrip()
    if data == '.':
        break
    stack = []
    result = 'yes'
    for i in data:
        if i in '([':
            stack.append(i)
        elif i in ')]':
            if not stack:
                result = 'no'
                break
            else:
                check = stack.pop()
                if i == ')' and check != '(':
                    result = 'no'
                    break
                elif i == ']' and check != '[':
                    result = 'no'
                    break
    if stack:
        result = 'no'
    print(result)
    stack.clear()