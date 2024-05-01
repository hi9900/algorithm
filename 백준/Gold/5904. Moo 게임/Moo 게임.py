# 총 수열 길이, 가운데 수열 길이, 구하려는 순서
def solve(total_length, mid_length, N):
    if N <= 3:
        return 'moo'[N-1]

    before_length = (total_length - mid_length) // 2
    # 왼쪽
    if N <= before_length:
        return solve(before_length, mid_length - 1, N)
    # 오른쪽
    if total_length - before_length < N:
        return solve(before_length, mid_length - 1, N - before_length - mid_length)
    # 가운데
    if N == before_length + 1:
        return 'm'
    else:
        return 'o'


N = int(input())

# 1. 몇 번째 수열인 지 구하기
# S(k)의 길이 = S(k-1)의 길이 * 2 + 가운데 수열의 길이
# 가운데 길이 = 3 + 수열의 순서 k
total_length = 3    # S(0) = moo -> 3
k = 0
while total_length < N:
    k += 1
    total_length = 2 * total_length + k + 3

# 2. N 위치의 수열까지 줄여나가기
print(solve(total_length, k + 3, N))