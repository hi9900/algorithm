import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(N):
    lst = list(map(int, input().split()))
    slst = set(lst)
    lst.sort()
    if len(slst) == 1:
        result = max(result, (10000 + lst[0] * 1000))
    elif len(slst) == 2:
        result = max(result, (1000 + lst[1] * 100))
    else:
        result = max(result, lst[2]*100)
print(result)