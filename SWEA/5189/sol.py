import sys
sys.stdin = open("input.txt")


def cart(s, ans):
    global result
    if ans >= result:
        return

    if sum(visited) == (N-1):
        result = min(ans+data[s][0], result)

    for j in range(1, N):
        if data[s][j] > 0 and not visited[j]:
            visited[j] = 1
            cart(j, ans+data[s][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 10e9

    cart(0, 0)
    print(f"#{tc} {result}")
