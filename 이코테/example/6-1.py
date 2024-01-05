def search_store(array, target, start, end):
    if start > end:
        return 'no'

    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] < target:
        return search_store(array, target, mid+1, end)
    elif array[mid] > target:
        return search_store(array, target, start, mid-1)


N = int(input())
stores = list(map(int, input().split()))
# 이진 탐색을 수행하기 위해 정렬
stores.sort()

M = int(input())
wishes = list(map(int, input().split()))

ans = []
# 구매할 부품을 하나씩 타겟으로 하여 가게 안에 있는지 확인한다.
for wish in wishes:
    ans.append(search_store(stores, wish, 0, N-1))

print(*ans)
