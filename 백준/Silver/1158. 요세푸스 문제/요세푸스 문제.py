import sys
input = sys.stdin.readline

N, K = map(int, input().split())

out = 0
arr = list(range(1, N+1))
result = []

for i in range(N):
    out += K-1
    if out >= len(arr):
        out %= len(arr)
    result.append(str(arr.pop(out)))

print(f'<{", ".join(result)}>')