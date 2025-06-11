import sys
input = sys.stdin.readline

pipe = input().strip()

prev = ''
temp = 0
cnt = 0
for p in pipe:
    if p == "(":
        temp += 1
    else:
        if prev == '(':
            temp -= 1
            cnt += temp
        else:
            temp -= 1
            cnt += 1

    prev = p

print(cnt)
