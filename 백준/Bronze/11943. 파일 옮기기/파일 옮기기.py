import sys
input = sys.stdin.readline

fst = list(map(int, input().split()))
scd = list(map(int, input().split()))

"""
두 종류의 과일을 옮기는 경우는 두 가지 밖에 없다.
1. 첫 번째 바구니에 사과, 두 번째 바구니에 오렌지
2. 첫 번째 바구니에 오렌지, 두 번째 바구니에 사과

두 경우중 적은 횟수를 고른다.
"""

print(min(fst[0] + scd[1], fst[1] + scd[0]))
