numbers = input().split('-')
ans = 0
for i, plus in enumerate(numbers):
    tmp = sum(map(int, plus.split('+')))
    if i == 0:
        ans += tmp
    else:
        ans -= tmp
print(ans)