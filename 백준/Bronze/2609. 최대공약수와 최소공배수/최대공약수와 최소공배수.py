import sys
input = sys.stdin.readline

A, B = map(int, input().split())

for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        # 최대 공약수
        a = i
        # 최소 공배수
        b = a * A//i * B//i
        break

print(a)
print(b)