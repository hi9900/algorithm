import sys
input = sys.stdin.readline

N = int(input())

data = [0] * 501
data[0] = 1
data[1] = 1

for i in range(2, N+1):
    if data[i] == 0:
        data[i] = data[i-1] * i

fact_n = data[N]
cnt = 0
while 1:
    fact_n, a = divmod(fact_n, 10)

    if a != 0:
        print(cnt)
        break

    cnt += 1
