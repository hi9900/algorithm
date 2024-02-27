N = int(input())
data = []
for _ in range(N):
    s, e = map(int, input().split())
    data.append((s, e))

data.sort(reverse=True)

cnt = 0
# 뒤에서부터 시작 시간을 찾음
# 시작 시간이 가장 느린 것
start = 2**31
for s, e in data:
    # 시작 시간이 느리고,
    # 이전 시작 시간보다 종료 시간이 빠르면 추가
    if start >= e:
        start = s
        cnt += 1

print(cnt)
