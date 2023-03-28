import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = 0
for i in range(1, n-1):
    a += i * (n-i-1)

print(a)
print(3)
