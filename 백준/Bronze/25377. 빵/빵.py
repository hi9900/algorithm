import sys
input = sys.stdin.readline

N = int(input())
result = 10000
for _ in range(N):
    # 가게까지 시간 A, 빵이 들어올 때 까지 시간 B
    A, B = map(int, input().split())

    # 빵이 오기전에 가게에 도착하거나
    # 빵이 오는 순간에 정확히 맞춰 와야 한다.
    if A <= B:
        result = min(result, B)

print(-1) if result == 10000 else print(result)
