N, K = map(int, input().split())

# 1. N -= 1
# 2. N //= K

num = 0
while 1:
    if N == 1:
        break
    # N이 K로 나누어 떨어지지 않으면 1번
    if N % K:
        N -= 1
    # 나누어 떨어지면 2번
    else:
        N //= K
    num += 1
print(num)

# N이 큰 수일때,
result = 0
while 1:
    # K로 나누어 떨어지는 수가 될 때까지 1 빼기
    target = (N // K) * K
    result += (N - target)
    N = target

    # N이 K보다 작으면, 반복문 탈출
    if N < K:
        break
    # K로 나누기
    result += 1
    N //= K
# 마지막 남은 수에 대해 1까지 되도록 빼기
result += (N - 1)
print(result)

