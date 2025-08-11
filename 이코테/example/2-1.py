N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

'''
# 1번 풀이. m의 크기가 커지면 시간초과
numbers.sort(reverse=True)

ans = 0
count = 0

for _ in range(M):
    if count == K:
        ans += numbers[1]
        count = 0
    else:
        ans += numbers[0]
        count += 1

print(ans)
'''

# 2번 풀이. 수열 적용
# M 안에서 K+1이 들어갈 수 있는 횟수
max = M // (K+1)
# 그러고 남은 갯수
plus = M % (K+1)

numbers.sort(reverse=True)
# 제일 큰 수
number_fst = numbers[0]
# 다음 큰 수
number_snd = numbers[1]

print(number_fst * K * (max + plus) + number_snd * max)