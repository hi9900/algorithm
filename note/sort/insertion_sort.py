# 삽입 정렬(insertion sort)
# 데이터를 하나씩 확인하며 적절한 위치에 삽입

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
N = len(arr)

for i in range(1, N):
    for j in range(i, 0, -1):       # i부터 1까지 감소
        if arr[j] < arr[j - 1]:     # 큰 데이터를 만나면 왼쪽으로 한 칸씩 이동
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:   # 작은 데이터를 만나면, 그 위치에서 종료 
            break

print(arr)
