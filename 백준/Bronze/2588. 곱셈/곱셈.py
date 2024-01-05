import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# N, M은 모두 세자리 수
# 1. N * M의 1의자리
# 2. N * M의 10의 자리
# 3. N * M의 100의 자리
# 4. N * M

print(N * (M % 10))
print(N * ((M % 100) // 10))
print(N * (M // 100))
print(N * M)
