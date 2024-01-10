import sys
input = sys.stdin.readline

"""
N개의 바구니
공이 1개씩 들어있음, 바구니와 같은 번호공

M번 공을 바꾼다.
바구니 2개의 공을 서로 교환
"""

N, M = map(int, input().split())
arr = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i],

print(*arr[1:])