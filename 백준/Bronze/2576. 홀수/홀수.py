import sys
input = sys.stdin.readline

sum_n = 0
min_n = 100
for _ in range(7):
    num = int(input())

    if num % 2:
        sum_n += num
        min_n = min(min_n, num)

print(sum_n, min_n, sep='\n') if sum_n > 0 else print(-1)
