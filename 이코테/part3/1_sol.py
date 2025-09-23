N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
group = 0   # 한 그룹에 속한 인원

for i in range(N):
    x = arr[i]
    group += 1  # 그룹에 추가

    if group >= arr[i]:   # 최대 공포도가 그룹 인원보다 크면 그룹 결성
        result += 1
        group = 0

print(result)
