# 재귀함수로 구현한 이진탐색
def binary_search(array, target, start, end):
    # 탐색 실패
    if start > end:
        return None

    # 중간점
    mid = (start + end) // 2
    
    # 타겟을 찾으면 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점보다 타겟이 작으면 왼쪽 탐색
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점보다 타겟이 크면 오른쪽 탐색
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)


n, t = 10, 4
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search(arr, t, 0, n-1)

print("없음" if result == None else result)
