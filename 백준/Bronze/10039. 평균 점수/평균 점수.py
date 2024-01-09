import sys
input = sys.stdin.readline

scores = [40] * 5

for _ in range(5):
    score = int(input())
    if score >= 40:
        scores[_] = score

print(int(sum(scores) / 5))