N = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    # 만들 수 없다면 종료
    if target < x:
        break
    target += x

print(target)
