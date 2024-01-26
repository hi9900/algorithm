import sys
input = sys.stdin.readline

X = int(input())

line = 0
end = 0
while 1:
    line += 1
    end += line

    if X <= end:
        break

start = end - line + 1
diff = X - start

# 위 대각선
if line % 2:
    # 시작 좌표 = line, 1
    target = (line-diff, 1+diff)
# 아래 대각선
else:
    # 시작 좌표 = 1, line
    target = (1+diff, line-diff)

print(*target, sep="/")
