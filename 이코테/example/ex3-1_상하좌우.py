N = int(input())
todo = list(map(str, input().split()))

# L 왼쪽, R 오른쪽, U 위로, D 아래로
dxy = {'L': (0, -1),
       'R': (0, 1),
       'U': (-1, 0),
       'D': (1, 0)}

sx, sy = 0, 0

for i in todo:
    dx, dy = dxy[i]
    nx, ny = sx + dx, sy + dy

    # 공간 밖이면 이동하지 않음
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
    
    # 이동한 그 자리에서 다시 출발
    sx, sy = nx, ny

# 0, 0에서 시작했으므로 1, 1씩 더해줌
print(sx+1, sy+1)
