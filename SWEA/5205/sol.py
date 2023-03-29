import sys
sys.stdin = open("input.txt")


def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j


def quickSort(A, l, r):
    if len(A[l:r+1]) == 0:
        return
    s = partition(A, l, r)
    quickSort(A, l, s-1)
    quickSort(A, s+1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A_lst = list(map(int, input().split()))
    quickSort(A_lst, 0, N-1)
    print(f"#{tc} {A_lst[N // 2]}")
