import sys
input = sys.stdin.readline

R1, S = map(int, input().split())

# S = (R1 + R2) / 2
# 2S = R1 + R2
# R2 = 2S - R1
print(2*S - R1)