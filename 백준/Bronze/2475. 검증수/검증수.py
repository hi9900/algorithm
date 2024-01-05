import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))

ans = 0
for number in numbers:
    # 제곱한 수의 합
    ans += number ** 2

print(ans % 10)
