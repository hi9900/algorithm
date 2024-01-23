import sys
input = sys.stdin.readline

# 0, 0
cnt = 0
for i in range(8):
    data = input().rstrip()
    for j in range(8):
        if (i + j) % 2 == 0 and data[j] == 'F':
            cnt += 1

print(cnt)