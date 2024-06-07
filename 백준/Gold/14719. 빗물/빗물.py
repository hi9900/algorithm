H, W = map(int, input().split())
blocks = list(map(int, input().split()))
result = 0

# 양 끝 제외
for i in range(1, W-1):
    # blocks[i]를 기준으로 왼 / 오른쪽 최대
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])

    rain = min(left_max, right_max) - blocks[i]
    if rain > 0:
        result += rain

print(result)