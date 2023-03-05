import sys
input = sys.stdin.readline

K_melon = int(input())
arrow = []
length = []
data = []
cnt = [0] * 5

for _ in range(6):
    a, l = map(int, input().split())
    arrow.append(a)
    cnt[a] += 1
    length.append(l)

big = 1
small = 1
for i in range(6):
    if cnt[arrow[i]] == 1:
        big *= length[i]

for i in range(6):
    back = (i-1) % 6
    front = (i+1) % 6
    if arrow[back] == arrow[front]:
        small *= length[i]

print((big-small)*K_melon)


