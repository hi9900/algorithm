import sys
input = sys.stdin.readline

"""
N개의 바구니
1 ~ N 번의 번호 공
첫 바구니는 비어있고, 바구니에는 공 1개만

M번 공을 넣을 거임
공을 넣을 바구니 범위(연속)를 정하고
같은 번호의 공을 바구니에 넣는다.
    이미 공이 들어 있다면, 빼고 새 공을 넣는다.

M번 공을 넣은 후에 바구니의 상태
"""

N, M = map(int, input().split())

arr = [0] * (N + 1)

for _ in range(M):
    # i번 ~ j번 바구니에 k번 공을 넣는다.
    i, j, k = map(int, input().split())

    for x in range(i, j+1):
        arr[x] = k

print(*arr[1:])