import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(input().strip()) for _ in range(8)]
    data_t = list(zip(*data))

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            check = data[i][j:j+N]
            if check == check[::-1]:
                cnt += 1

            check_t = data_t[i][j:j+N]
            if check_t == check_t[::-1]:
                cnt += 1
    print(f"#{tc} {cnt}")
