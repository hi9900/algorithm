# 반복문으로 구현한 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 중간점이 타겟이면, 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점이 타겟보다 크면, 왼쪽 탐색
        elif array[mid] > target:
            end = mid - 1
        # 중간점이 타겟보다 작으면, 오른쪽 탐색
        elif array[mid] < target:
            start = mid + 1

    # 타겟이 없음
    return None

n, t = 10, 9
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search(arr, t, 0, n-1)

print("없음" if result == None else result)

