import sys
input = sys.stdin.readline

n = int(input())
house_r = list(map(int, input().split()))

# 난로의 반지름의 약수가 동일한 집들은 함께 사용 가능
# check[i] = i를 약수로 가지는 집의 수
check = [0] * 101

for house in house_r:
    # 연탄 반지름은 항상 1보다 커야한다.
    for i in range(2, house+1):
        if house % i == 0:
            check[i] += 1

print(max(check))
