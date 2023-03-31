import sys
sys.stdin = open("input.txt")


def m_cost(N, i, ans):
    global cost

    if ans >= cost:
        return

    if sum(check) == N:
        cost = min(cost, ans)

    for j in range(N):
        if not check[j]:
            check[j] = 1
            m_cost(N, i+1, ans + data[i][j])
            check[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    cost = 10e9

    m_cost(N, 0, 0)
    print(f"#{tc} {cost}")
