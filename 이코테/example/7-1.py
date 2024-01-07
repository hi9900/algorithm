X = int(input())

# X의 최대 범위 30000
d = [0] * 30001

for i in range(2, X+1):
    # +1: 횟수 증가
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[X])
