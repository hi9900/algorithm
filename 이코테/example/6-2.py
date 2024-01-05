N, M = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, max(data)
H = 0
while 1:
    if start > end:
        break

    mid = (start + end) // 2
    total = 0
    # 떡을 하나씩 잘라서 더하기
    for x in data:
        if x > mid:
            total += x - mid
        
    # 자른 떡이 필요한 길이보다 작으면, 왼쪽으로
    if total < M:
        end = mid - 1
    # 자른 떡이 필요한 길이보다 크다면, 기록 후 오른쪽으로
    # 최대한 덜 잘라야 하므로 기록한 뒤 딱 맞춰 자르지 못했을 때 그 값이 정답
    elif total > M:
        H = mid
        start = mid + 1
    # 딱 맞춰서 잘랐다면, 최선이므로 반복문 종료
    elif total == M:
        H = mid
        break

print(H)
