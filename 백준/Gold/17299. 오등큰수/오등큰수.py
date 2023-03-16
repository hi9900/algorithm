import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 1000001

data = list(map(int, input().split()))
data_cnt = [0] * N

result = [-1] * N
for i in data:
    cnt[i] += 1
    
for i in range(N):
    data_cnt[i] = cnt[data[i]]

stack = [[data_cnt.pop(), N-1]]

for i in range(N-2, -1, -1):
    while 1:
        if not stack:
            break
        if stack[-1][0] > data_cnt[-1]:
            result[i] = data[stack[-1][1]]
            break
        else:
            stack.pop()

    stack.append([data_cnt.pop(), i])

print(*result)


