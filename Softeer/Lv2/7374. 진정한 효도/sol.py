import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(3)]

# 가로 또는 세로 3칸 땅 높이가 동일
cost = 10

for i in range(3):
    # 가로 확인
    a = data[i][0]
    b = data[i][1]
    c = data[i][2]
    if len({a, b, c}) == 1:
        cost = 0
        break
    # 빈도가 적은 높이를 다른 높이에 맞추기
    elif len({a, b, c}) == 3: # 1 2 3
        cost = min(cost, 2)
    else: 
        cost = min(cost, max(a, b, c) - min(a, b, c))
    
    # 세로 확인
    d = data[0][i]
    e = data[1][i] 
    f = data[2][i]
    if len({d, e, f}) == 1:
        cost = 0
        break
    elif len({d, e, f}) == 3:
        cost = min(cost, 2)
    else: 
        cost = min(cost, max(d, e, f) - min(d, e, f))
    
print(cost)