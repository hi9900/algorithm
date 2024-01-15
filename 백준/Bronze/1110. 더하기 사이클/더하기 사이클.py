import sys
input = sys.stdin.readline

N = int(input())
ori_n = N
cnt = 0
while 1:
    # 각 자리 수 더하기
    if N < 10:
        sum_n = N
    else:
        sum_n = N // 10 + N % 10
    # 이어 붙이기
    N = int(str(N)[-1] + str(sum_n)[-1])
    cnt += 1

    if ori_n == N:
        print(cnt)
        break
