# https://www.acmicpc.net/problem/2304
import sys
input = sys.stdin.readline

N = int(input())
data = [0] * 1001
max_L = 0
# data = []
for _ in range(N):
    # 왼쪽면 위치, 높이
    L, H = map(int, input().split())
    data[L] = H
    if L > max_L:
        max_L = L

max_h = max(data)
max_idx = data.index(max_h)
data_f = data[:max_idx+1]
data_b = data[max_L:max_idx:-1]

result = 0
save = 0
for i in range(len(data_f)):
    if data_f[i] >= save:
        save = data_f[i]
    result += save

save = 0
for i in range(len(data_b)):
    if data_b[i] >= save:
        save = data_b[i]
    result += save

print(result)
