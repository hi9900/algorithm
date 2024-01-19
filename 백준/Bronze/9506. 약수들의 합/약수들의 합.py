import sys
input = sys.stdin.readline

# 자신을 제외한 모든 약수들의 합
while 1:
    n = int(input())
    if n == -1:
        break

    lst = []
    sum_n = 0
    for i in range(1, n):
        if n % i == 0:
            sum_n += i
            lst.append(i)

    if sum_n == n:
        print(n, '=', end=" ")
        print(*lst, sep=" + ")
    else:
        print(f'{n} is NOT perfect.')
        