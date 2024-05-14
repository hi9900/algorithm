for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_result = [0] * N

    arr.sort()
    idx = 0
    for i in range(0, N, 2):
        arr_result[idx] = arr[i]
        idx += 1
        if i+1 < N:
            arr_result[-idx] = arr[i+1]

    result = 0
    for i in range(1, N):
        result = max(result, abs(arr_result[i] - arr_result[i-1]))

    print(result)
