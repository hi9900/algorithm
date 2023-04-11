import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
next = 6

check = 1
while 1:
    if cnt >= N:
        break
    check += 1
    cnt += next
    next += 6
print(check)
