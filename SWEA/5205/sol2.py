import sys
sys.stdin = open("input.txt")


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        else:
            left.append(arr[i])
    return [*quickSort(left), pivot, *quickSort(right)]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst_s = quickSort(lst)
    print(f"#{tc} {lst_s[N // 2]}")