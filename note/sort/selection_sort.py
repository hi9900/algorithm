# 선택 정렬(selection sort)
# 가장 작은 것을 선택해 앞으로 보내는 과정을 반복

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
N = len(arr)

for i in range(N):
    # 가장 작은 원소
    min_idx = i

    for j in range(i + 1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j

    # swap
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
