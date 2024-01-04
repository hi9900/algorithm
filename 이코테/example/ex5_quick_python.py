arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    # 원소가 하나 이하이면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    # 분할된 왼쪽 리스트: 피벗보다 작은 데이터
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 리스트: 피벗보다 큰 데이터
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))