
# 정렬을 수행할 리스트, 시작 인덱스, 끝 인덱스
def quick_sort(arr, start, end):
    # 원소가 1개라면, 종료
    if start >= end:
        return

    # 피벗은 첫 번째 인덱스
    pivot = start
    left = start+1
    right = end

    while 1:
        # 왼쪽에서부터 피벗보다 큰 데이터
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 오른쪽에서부터 피벗보다 작은 데이터
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 두 값이 엇갈렸다면, 작은 데이터와 피벗을 교체 후 분할
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            break
        # 엇갈리지 않았다면, 큰 데이터와 작은 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 후 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr)-1)
print(arr)
