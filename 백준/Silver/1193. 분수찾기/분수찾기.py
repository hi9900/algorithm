import sys
input = sys.stdin.readline

X = int(input())

# 분자, 분모
x, y = 1, 1
cnt = 1

while 1:
    if cnt == X:
        break
    cnt += 1
    if (x+y) % 2 == 1:
        if y == 1:
            x += 1
        else:
            x += 1
            y -= 1
    else:
        if x == 1:
            y += 1
        else:
            x -= 1
            y += 1

print(f"{x}/{y}")
