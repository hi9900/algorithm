import sys
input = sys.stdin.readline

M, N = map(int, input().split())
store = int(input())
stores = []
for _ in range(store):
    s, d = map(int, input().split())
    stores.append((s, d))

dong = list(map(int, input().split()))

result = 0
for st in stores:
    # 같은 방향
    if dong[0] == st[0]:
        result += abs(dong[1]-st[1])
    elif dong[0] == 1:
        if st[0] == 3:
            result += dong[1] + st[1]
        elif st[0] == 4:
            result += (M-dong[1]) + st[1]
        elif st[0] == 2:
            result += N + min(dong[1] + st[1], M-dong[1] + M-st[1])
    elif dong[0] == 2:
        if st[0] == 3:
            result += dong[1] + (N-st[1])
        elif st[0] == 4:
            result += (M-dong[1]) + (N-st[1])
        elif st[0] == 1:
            result += N + min(dong[1] + st[1], M-dong[1] + M-st[1])
    elif dong[0] == 3:
        if st[0] == 1:
            result += dong[1] + st[1]
        elif st[0] == 2:
            result += (N-dong[1]) + st[1]
        elif st[0] == 4:
            result += M + min(dong[1] + st[1], N-dong[1] + N-st[1])
    elif dong[0] == 4:
        if st[0] == 1:
            result += dong[1] + (M-st[1])
        elif st[0] == 2:
            result += (N-dong[1]) + (M-st[1])
        elif st[0] == 3:
            result += M + min(dong[1] + st[1], N-dong[1] + N-st[1])

print(result)
