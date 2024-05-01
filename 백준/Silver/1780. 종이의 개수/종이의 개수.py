def is_same_number(num, si, sj, l):
    global data
    for x in range(si, si + l):
        for y in range(sj, sj + l):
            if data[x][y] != num:
                return False
    return True


def solve(si, sj, l):
    global data, result
    num = data[si][sj]

    if l == 1:
        result[num] += 1
        return

    # 1. 모든 종이가 같은 수로 되어 있다면, 이 종이를 그대로 사용 한다.
    if is_same_number(num, si, sj, l):
        result[num] += 1
        return
    else:   # 2. 종이를 같은 크기의 종이 9개로 자른다.
        for i in range(si, si + l, l // 3):
            for j in range(sj, sj + l, l // 3):
                solve(i, j, l // 3)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

result = {
    -1: 0,
    0: 0,
    1: 0
}
solve(0, 0, N)
print(*result.values())
