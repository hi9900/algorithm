# 퀵 정렬(quick sort)
# 기준 데이터(pivot)를 설정하고
# 그 기준보다 큰 데이터와 작은 데이터의 위치를 교환한 후
# 리스트를 반으로 나누는 방식


# 정렬할 리스트, 시작인덱스, 끝인덱스
def quick_sort(arr, start, end):
    # 종료조건: 원소가 1개
    if start >= end:
        return 

    pivot = start
    left, right = start + 1, end
    
    while True:
        # 왼쪽에서부터 피벗보다 큰 데이터 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 오른쪽에서부터 피벗보다 작은 데이터 찾기
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 두 값이 엇갈리면, 분할
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            break
        # 엇갈리지 않으면, 교체
        else:
            arr[left], arr[right] = arr[right], arr[left],

    # 분할 리스트 재정렬
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
N = len(arr)
quick_sort(arr, 0, N - 1)
print(arr)
