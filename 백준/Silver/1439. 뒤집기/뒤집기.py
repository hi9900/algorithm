import sys
input = sys.stdin.readline

S = list(map(int, input().rstrip()))
counts = [0, 0]
N = len(S)

for i in range(1, N):
    if S[i-1] != S[i]:
        counts[S[i-1]] += 1

counts[S[N-1]] += 1
print(min(counts))
