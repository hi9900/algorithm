arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    # 인덱스 i부터 1까지 감소하며 반복
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        # 작은 데이터를 만나면, 그 위치에 삽입
        else:
            break

print(arr)
