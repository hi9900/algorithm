import sys
input = sys.stdin.readline

A, B = map(str, input().split())

# 수 뒤집기
A = A[::-1]
B = B[::-1]

# 큰 수 출력
print(max(int(A), int(B)))