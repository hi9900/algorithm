def hanoi(k, s, m, e):
    global cnt
    if k == 1:
        cnt += 1
        result.append((s, e))
        return

    hanoi(k-1, s, e, m)
    hanoi(1, s, m, e)
    hanoi(k-1, m, s, e)


N = int(input())
cnt = 0
result = []
hanoi(N, 1, 2, 3)
print(cnt)
for i in range(cnt):
    print(*result[i])