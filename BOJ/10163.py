# https://www.acmicpc.net/problem/10163
import sys
input = sys.stdin.readline

N = int(input())
data = [[0] * 1002 for _ in range(1002)]
cnt_l = []
paper = []
for p in range(N):
    sj, si, b, h = map(int, input().split())
    paper.append((si, sj, b, h, p+1))
while paper:
    si, sj, b, h, p = paper.pop()
    cnt = 0
    for i in range(si, si+h):
        for j in range(sj, sj+b):
            if data[i][j] == 0:
                data[i][j] = p
                cnt += 1
    cnt_l.append(cnt)
print(data)
print(*cnt_l[::-1], sep="\n")