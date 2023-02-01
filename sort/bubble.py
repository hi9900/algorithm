# 배열을 활용한 버블정렬(오름차순)

# 정렬할 리스트(배열) a, 원소 수(배열의 크기) N
def BubbleSort(a, N):
    # N = len(a)
    # 정렬완료 될 index(i) 순서: N-1 -> 1
    for i in range(N-1, 0, -1):
        # 비교할 원소 중 왼쪽 원소의 인덱스(j): 0 -> 정렬완료된 인덱스 전까지 == i-1
        for j in range(0, i):
            # 왼쪽 원소가 더 크면,
            if a[j] > a[j+1]:
                # 오른쪽 원소와 자리 교체
                a[j], a[j+1] = a[j+1], a[j]
    return a
