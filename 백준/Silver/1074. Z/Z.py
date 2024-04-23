def solve(n, r, c, num):
    if n == 0:
        print(num)
        return

    div = 2 ** (n - 1)
    # 위치 찾기
    if r < div and c < div:
        solve(n - 1, r, c, num)
    elif r < div and c >= div:
        solve(n - 1, r, c - div, num + div ** 2)
    elif r >= div and c < div:
        solve(n - 1, r - div, c, num + 2 * div ** 2)
    elif r >= div and c >= div:
        solve(n - 1, r - div, c - div, num + 3 * div ** 2)

        
N, r, c = map(int, input().split())
solve(N, r, c, 0)
