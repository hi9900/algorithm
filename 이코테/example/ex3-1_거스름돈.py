# 거슬러 줘야 할 돈 N
N = int(input())

# 동전 갯수
ans = 0

# 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전
coins = [500, 100, 50, 10]

for coin in coins:
    # 줄 수 있는 만큼의 동전 갯수
    ans += N//coin
    N %= coin

print(ans)
