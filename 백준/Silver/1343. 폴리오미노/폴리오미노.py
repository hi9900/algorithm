import sys
input = sys.stdin.readline

mino = ['AAAA', 'BB']
data = input()
result = []
cnt = 0
for i in data:
    if i == 'X':
        cnt += 1
    else:
        if cnt == 0:
            result.append(i)
            continue
        if cnt % 4 == 0:
            result.append(mino[0] * (cnt // 4))
        elif cnt % 2 == 0:
            x, y = divmod(cnt, 4)
            result.append(mino[0] * x + mino[1])
        else:
            result = -1
            break
        cnt = 0
        if i == '.':
            result.append(i)

else:
    result = ('').join(result)

print(result)
