import sys
input = sys.stdin.readline

y, m, d = map(int, input().split())
yy, mm, dd = map(int, input().split())

# 만나이, 생일을 기준으로 계산
# 생일이 지났으면
if m < mm or (m == mm and d <= dd):
    print(yy - y)
# 생일 안 지났으면
else:
    print(yy - y - 1)

# 세는 나이, 생년을 기준으로
print(yy - y + 1)

# 연 나이, 현재 연도에서 생년을 뺀 값
print(yy - y)