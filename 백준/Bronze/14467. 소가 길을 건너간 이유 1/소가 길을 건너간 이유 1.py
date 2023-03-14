import sys
input = sys.stdin.readline

N = int(input())
cow_w = [-1] * 11
cnt = 0
for _ in range(N):
    cow, d = map(int, input().split())
    if cow_w[cow] != -1:
        if cow_w[cow] != d:
            cnt += 1

    cow_w[cow] = d

print(cnt)
