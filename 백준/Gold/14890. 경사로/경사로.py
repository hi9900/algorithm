def solve(arr):
    global cnt

    for i in range(N):
        check = [0] * N
        check[0] = 1
        isStop = False
        for j in range(1, N):

            if check[j] == -1:
                continue
            # 이전 칸과 차이가 1칸 초과면 ㄴㄴ
            if abs(arr[i][j-1] - arr[i][j]) > 1:
                break
            # 이전 칸과 높이가 같으면
            if arr[i][j-1] == arr[i][j]:
                check[j] = check[j-1] + 1
                continue
            # 이전 보다 한 칸 높으면, 낮은 칸(이전)의 개수가 L개 이상
            elif arr[i][j] - arr[i][j-1] == 1:
                if check[j - 1] < L:
                    break
                for k in range(L):
                    check[j - 1 - k] = -1
                check[j] = 1

            # 이전 칸보다 한 칸 낮으면, L만큼 경사로
            elif arr[i][j-1] - arr[i][j] == 1:
                for k in range(L):
                    if j + k < N and arr[i][j] == arr[i][j+k]:
                        check[k] = -1
                    else:
                        isStop = True
                        break
                if isStop:
                    break
        else:
            cnt += 1


N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

lst_r = list(zip(*lst))
cnt = 0

solve(lst)
solve(lst_r)

print(cnt)
