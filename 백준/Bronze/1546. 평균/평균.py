import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

M = max(score)
sum_s = 0
for i in range(N):
    sum_s += score[i] / M * 100

print(sum_s / N)