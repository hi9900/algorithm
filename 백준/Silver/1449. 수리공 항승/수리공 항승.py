import sys
input = sys.stdin.readline

N, L = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

tape = data[0] - 0.5 + L
cnt = 1
for i in range(1, N):
    # 테이프 같이 붙음
    if data[i] <= tape:
        pass
    else:
        tape = data[i] - 0.5 + L
        cnt += 1

print(cnt)