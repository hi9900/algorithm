# 계수 정렬(count sort)
# 데이터의 등장 횟수를 기록한 후, 그 값만큼 인덱스를 출력

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
N = len(arr)

# 등장 횟수 기록
count = [0] * (max(arr) + 1)

for a in arr:
    count[a] += 1

# 등장 횟수만큼 출력
for i in range(max(arr) + 1):
    for j in range(count[i]):
        print(i, end=" ")
