import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

time, height = 10e9, -1

for h in range(257):    # 도달 높이 h
    up_block, down_block = 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > h:
                # 1. 블록 제거
                down_block += arr[i][j] - h
            else:
                # 2. 블록 놓기
                up_block += h - arr[i][j]

    # 높이 h로 만들 수 있음
    if down_block + B >= up_block:
        if time >= down_block * 2 + up_block:
            time = down_block * 2 + up_block
            height = h

print(time, height)