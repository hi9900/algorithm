import sys
input = sys.stdin.readline

# 소 N마리, 헛간 W x H, 공간 L
N, W, H, L = map(int, input().split())

print(min((W // L) * (H // L), N))
