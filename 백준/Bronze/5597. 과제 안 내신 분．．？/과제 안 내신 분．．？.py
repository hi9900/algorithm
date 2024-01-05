import sys
input = sys.stdin.readline

students = [0] * 31

for _ in range(28):
    students[int(input())] += 1

cnt = 0
for i in range(1, 32):
    if cnt == 2:
        break
    if students[i] == 0:
        print(i)
        cnt += 1
