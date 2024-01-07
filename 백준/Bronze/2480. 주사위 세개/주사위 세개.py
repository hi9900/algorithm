import sys
input = sys.stdin.readline

data = list(map(int, input().split()))

cnt = set(data)

# 같은 눈 3개
if len(cnt) == 1:
    print(10000 + data[0] * 1000)
# 같은 눈 2개
elif len(cnt) == 2:
    # 같은 눈 찾기
    for i in cnt:
        if data.count(i) == 2:
            print(1000 + i * 100)
            break
# 같은 눈 없음
else:
    print(max(data) * 100)

