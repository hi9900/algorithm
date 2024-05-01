import sys
input = sys.stdin.readline

def solve(n):
    global A, C
    if n == 1:
        return A % C

    half = solve(n // 2)
    if n % 2:
        return (half * half * A) % C
    return (half * half) % C


A, B, C = map(int, input().split())
print(solve(B))
