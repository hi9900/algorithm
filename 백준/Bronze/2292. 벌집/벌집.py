import sys
input = sys.stdin.readline

N = int(input())

"""
1 -> 1
2 ~ 7 (6) -> 2
8 ~ 19 (12) -> 3
20 ~ 37 (18) -> 4
"""

cnt = 1
result = 1
while 1:
    if N <= cnt:
        break
    cnt += result * 6
    result += 1

print(result)
