import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    sum_lst = [0] * (N-M+1)

    for i in range(N-M+1):
        # print(i)
        sum_lst[i] = sum(data[i:i+M])

    # print(sum_lst)
    result = max(sum_lst) - min(sum_lst)
    print(f"#{tc} {result}")