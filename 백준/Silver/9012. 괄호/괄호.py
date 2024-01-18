import sys
input = sys.stdin.readline

# 괄호 문자열 VPS

T = int(input())
for _ in range(T):
    # 괄호 저장
    stack = []

    a = input().rstrip()
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')