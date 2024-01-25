import sys
input = sys.stdin.readline

"""
lst 갯수는 100,000
하나씩 검사하면 시간초과
---
1. 이분탐색
2. 집합 자료형
"""


# 이분탐색 알고리즘
def solution(s, e, target, lst):
    # 없음
    if s > e:
        return 0
    # 중간지점
    mid = (s + e) // 2
    # 비교
    if lst[mid] == target:
        return 1
    elif lst[mid] > target:
        # 왼쪽
        return solution(s, mid-1, target, lst)
    elif lst[mid] < target:
        # 오른쪽
        return solution(mid+1, e, target, lst)


N = int(input())
lst = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

# lst 정렬
lst.sort()

for i in check:
    print(solution(0, N-1, i, lst))