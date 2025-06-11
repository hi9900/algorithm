import sys
input = sys.stdin.readline

A, B, C = [input().strip() for _ in range(3)]

print(int(A) + int(B) - int(C))
print(int(A+B) - int(C))
