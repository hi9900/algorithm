import sys
input = sys.stdin.readline
sum = 0
for _ in range(5):
    x = int(input())
    sum += x if x >= 40 else 40
print(sum//5)