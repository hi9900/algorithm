# https://www.acmicpc.net/problem/2669
import sys
input = sys.stdin.readline

data = [[0] * 101 for _ in range(101)]
result = 0
for _ in range(4):
    sj, si, fj, fi = map(int, input().split())

    for i in range(si, fi):
        for j in range(sj, fj):
            if not data[i][j]:
                data[i][j] += 1
                result += 1
print(result)
