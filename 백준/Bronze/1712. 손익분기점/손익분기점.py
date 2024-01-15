import sys
input = sys.stdin.readline

# 고정비용 A, 가변비용 B, 판매 가격 C
A, B, C = map(int, input().split())

# 발생하지 않는 경우
if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)
