import itertools
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# M에 가장 가까운 3장의 합
# N개 중에서 3개 고르기 -> N C 3
max_result = 0
for i in list(itertools.combinations(cards, 3)):
    if sum(i) <= M:
        max_result = max(max_result, sum(i))

print(max_result)
