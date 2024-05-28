N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * 100_001
result = 0
start, end = 0, 0

while 1:
    if end > start or start >= N:
        break

    if cnt[arr[start]] < K:
        cnt[arr[start]] += 1
        start += 1

    else:
        cnt[arr[end]] -= 1
        end += 1

    result = max(result, start - end)

print(result)
