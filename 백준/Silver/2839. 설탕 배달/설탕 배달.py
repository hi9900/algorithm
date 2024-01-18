import sys
input = sys.stdin.readline

# 설탕 N
# 봉지 3, 5
# 최대한 적은 봉지

N = int(input())
cnt = 0


# 5로 최대로 나누었을 때, 나머지가 3의 배수이면 출력
a, b = divmod(N, 5)
if b % 3 == 0:
    print(a + b//3)
# 나머지가 3의 배수가 아니라면, 5로 나눈 몫을 하나씩 빼면서 검사
else:
    while a > 0:
        a -= 1
        b += 5
        if b % 3 == 0:
            print(a + b // 3)
            break
    else:
        print(-1)