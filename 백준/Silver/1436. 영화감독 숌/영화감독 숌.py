import sys
input = sys.stdin.readline

N = int(input())

i = 0
cnt = 0
while 1:
    i += 1
    if "666" in str(i):
        cnt += 1

    if cnt == N:
        print(i)
        break