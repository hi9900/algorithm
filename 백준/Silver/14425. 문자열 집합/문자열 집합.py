import sys
input = sys.stdin.readline

N, M = map(int, input().split())
text = []
for _ in range(N):
    text.append(input().rstrip())
text = set(text)
cnt = 0
for _ in range(M):
    if input().rstrip() in text:
        cnt += 1

print(cnt)