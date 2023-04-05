import sys
input = sys.stdin.readline


def perm(i, n, sm):
    global cnt

    if i == n:
        if sm == S:
            cnt += 1
        return

    perm(i+1, n, sm+data[i])
    perm(i+1, n, sm)


N, S = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
perm(0, N, 0)
if S == 0:
    cnt -= 1
    
print(cnt)