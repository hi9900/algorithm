import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
arr = list(map(int, input().split()))
cards = Counter(arr)

M = int(input())
check = list(map(int, input().split()))
for c in check:
    print(cards[c], end=" ")