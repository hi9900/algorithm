import sys
input = sys.stdin.readline

for _ in range(3):
    data = list(map(int, input().split()))
    # 등의 갯수
    check = sum(data)

    if check == 3:
        print('A')
    elif check == 2:
        print('B')
    elif check == 1:
        print('C')
    elif check == 0:
        print('D')
    elif check == 4:
        print('E')