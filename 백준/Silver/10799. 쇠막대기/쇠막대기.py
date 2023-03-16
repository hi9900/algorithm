import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []
result = 0
div = 0
for i in data:
    if i == "(":
        div += 1
    elif i == ")" and stack[-1] == "(":
        div -= 1
        result += div

    elif i == ")" and stack[-1] != "(":
        div -= 1
        result += 1
    stack.append(i)
print(result)


