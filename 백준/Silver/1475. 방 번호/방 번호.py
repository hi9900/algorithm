import sys
input = sys.stdin.readline

N = input().rstrip()
num = [0] * 10

for n in N:
    if int(n) == 9 or int(n) == 6:
        if num[6] > num[9]:
            num[9] += 1
        else:
            num[6] += 1

    else:
        num[int(n)]+= 1

print(max(num))
