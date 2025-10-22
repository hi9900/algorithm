# 왼쪽 90도 회전
def rotate(arr):
    L = len(arr)
    r_arr = [[0] * L for _ in range(L)]

    for i in range(L):
        for j in range(L):
            r_arr[L - j - 1][i] = arr[i][j]
    return r_arr


def check(arr, key, x, y, M, N):
    # arr 복사
    _arr = [[0] * (3 * N) for _ in range(3 * N)]
    for _ in range(3 * N):
        _arr[_][:] = arr[_][:]

    # 열쇠 끼워넣기
    for i in range(M):
        for j in range(M):
            _arr[x + i][y + j] += key[i][j]

    # 중앙이 모두 1인지 확인
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            if _arr[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 자물쇠 확장
    arr = [[0] * (3 * N) for _ in range(3 * N)]
    for i in range(N):
        for j in range(N):
            arr[i+N][j+N] = lock[i][j]

    # 회전하며 탐색
    for _ in range(4):
        key = rotate(key)

        for x in range(N * 2):
            for y in range(N * 2):
                if check(arr, key, x, y, M, N):
                    return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
