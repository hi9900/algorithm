import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print("")

# 소인수 분해
# N보다 작은 소수로 나누기
else:
    for i in range(2, N+1):
        if N == 1:
            break
        else:
            # i는 소수이므로, N에서 최대한 나누기
            # 소수가 아닌 수는 이미 나눠 졌으므로, 소수를 판별 할 필요가 없음
            while 1:
                if N % i == 0:
                    N //= i
                    print(i)
                else:
                    break
