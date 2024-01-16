import sys
input = sys.stdin.readline

cost = int(input())
money = 1000 - cost

# 가장 큰 돈부터 거슬러주기
arr = [500, 100, 50, 10, 5, 1]
result = 0
for i in arr:
    cnt, money = divmod(money, i)
    result += cnt

print(result)