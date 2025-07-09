n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def solve(r, c, k):
    gold = 0
    # 열
    for dr in range(-k, k+1):
        # 범위
        rem = k - abs(dr)
        rr = r + dr
        if rr < 0 or rr >= n:
            continue
        
        start = c - rem
        end = c + rem
        
        if start < 0:
            start = 0
        if end >= n:
            end = n - 1

        gold += sum(grid[rr][start:end+1])
    return gold


answer = 0
for i in range(n):
    for j in range(n):
        for k in range(2 * n):
            g = solve(i, j, k)
        
            if g * m >= k**2 + (k + 1)**2:
                answer = max(answer, g)

print(answer)