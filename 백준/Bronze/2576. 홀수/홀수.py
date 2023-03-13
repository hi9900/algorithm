
sum = 0
min_x = 99
for _ in range(7):
    x = int(input())
    if x % 2:
        sum += x
        min_x = min(min_x, x)

if sum != 0:
    print(sum)
    print(min_x)
else:
    print(-1)