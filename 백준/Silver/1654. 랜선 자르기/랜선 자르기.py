import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = [0] * K
for _ in range(K):
    line[_] = int(input())

# 이분탐색
# 가장 긴 랜선을 기준으로 반씩 나눈 값을 나머지 랜선에 적용
# 자른 개수가 N보다 크면 길이 출력
s, e = 1, max(line)
tmp = 0
while 1:
    mid = (s+e)//2
    if s > e:
        break

    cnt = 0
    for l in line:
        cnt += l // mid

    if cnt >= N:
        tmp = mid
        s = mid + 1
    else:
        e = mid - 1

print(e)