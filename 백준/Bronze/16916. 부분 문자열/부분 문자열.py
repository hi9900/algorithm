import sys
input = sys.stdin.readline

data = input().rstrip()
check = input().rstrip()

if check in data:
    print(1)
else:
    print(0)

