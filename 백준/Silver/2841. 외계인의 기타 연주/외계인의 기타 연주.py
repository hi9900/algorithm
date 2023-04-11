import sys
input = sys.stdin.readline

N, P = map(int, input().split())
data = [[] for _ in range(N+1)]
cnt = 0
for _ in range(N):
    num, pr = map(int, input().split())
    if not data[num]:
        data[num].append(pr)
        cnt += 1

    elif data[num][-1] < pr:
        data[num].append(pr)
        cnt += 1

    elif data[num][-1] > pr:
        while 1:
            if not data[num]:
                data[num].append(pr)
                cnt += 1
                break
            if data[num][-1] == pr:
                break
            if data[num][-1] < pr:
                data[num].append(pr)
                cnt += 1
                break
            data[num].pop()
            cnt += 1

    data[num].sort()

print(cnt)

