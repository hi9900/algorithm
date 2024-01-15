N = int(input())
arr = list(map(int, input().split()))

arr.sort()

# 총 그룹 수
result = 0
# 한 그룹에 속한 인원
cnt = 0
# 한 그룹의 최대 공포도
max_x = 0
for i in range(N):
    max_x = max(arr[i], max_x)
    cnt += 1

    # 사람수 >= 공포도인 순간, 그룹 결성
    if cnt >= max_x:
        result += 1
        cnt, max_x = 0, 0

print(result)