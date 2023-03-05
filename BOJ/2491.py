import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
cnt_up = [1] * N
cnt_dn = [1] * N

for i in range(1, N):
    if data[i-1] <= data[i]:
        cnt_up[i] += cnt_up[i-1]

    if data[i-1] >= data[i]:
        cnt_dn[i] += cnt_dn[i-1]

print(max(max(cnt_up), max(cnt_dn)))
