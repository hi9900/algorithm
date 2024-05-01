
# 모두 같은 색인지 확인
def is_same(i, j, n):
    for ii in range(i, i+n):
        for jj in range(j, j+n):
            if paper[ii][jj] != paper[i][j]:
                return -1
    return paper[i][j]


def solve(i, j, n):
    check = is_same(i, j, n)

    if check != -1:
        result[check] += 1
        return

    solve(i, j, n // 2)
    solve(i+n//2, j, n // 2)
    solve(i, j+n//2, n // 2)
    solve(i+n//2, j+n//2, n // 2)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 흰: 0, 파: 1
result = [0, 0]

solve(0, 0, N)
print(*result, sep='\n')
