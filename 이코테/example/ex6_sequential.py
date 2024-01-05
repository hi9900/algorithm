# 순차탐색 구현

# n 원소의 개수
# target 찾을 문자열
# array 문자열 배열
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # target을 찾았다면, 현재 위치 반환
        if array[i] == target:
            return i + 1
