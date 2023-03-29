import sys
input = sys.stdin.readline

result = 0
for _ in range(5):
    score = int(input())
    result += score
print(result)