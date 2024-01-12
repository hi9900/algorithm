import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(h-y, y, w-x, x))