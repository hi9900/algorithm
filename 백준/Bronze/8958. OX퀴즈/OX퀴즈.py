import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    result = list(input())

    arr = [0] * len(result)
    for i in range(len(result)):
        if result[i] == 'O':
            if arr[i-1] == 0:
                arr[i] = 1
            else:
                arr[i] = arr[i-1] + 1
        else:
            arr[i] = 0

    print(sum(arr))
