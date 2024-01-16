import sys
input = sys.stdin.readline

# N의 진짜 약수의 갯수
t = int(input())
# N의 진짜 약수들
lst = list(map(int, input().split()))

# N은 모든 lst의 배수이고, lst의 요소는 1과 N이 아니다.
# N: lst의 속한 원소들의 최소 공배수
#
print(max(lst) * min(lst))