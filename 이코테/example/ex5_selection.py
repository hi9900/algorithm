arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    # 가장 작은 원소의 인덱스
    min_idx = i

    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
