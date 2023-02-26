import pprint as pp
import sys
sys.stdin = open("input.txt")

T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    data_t = list(zip(*data))
    max_sum = 0
    cross_r = 0
    cross_l = 0
    # 가로, 세로
    for i in range(100):
        one = max(sum(data[i]), sum(data_t[i]))
        if one > max_sum:
            max_sum = one

    # 대각
        cross_r += data[i][i]
        cross_l += data[i][100-i-1]

    real_max = max(max_sum, cross_r, cross_l)
    print(f"#{tc} {real_max}")
