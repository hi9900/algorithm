import sys
input = sys.stdin.readline

H, M = map(int, input().split())

# 45분 전 알람
NH, NM = divmod(H * 60 + M - 45, 60)
if NH < 0:
    NH = 24 + NH

print(NH, NM)
