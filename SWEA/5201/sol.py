import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 화물
    w = list(map(int, input().split()))
    # 트럭
    t = list(map(int, input().split()))

    w_on = [0] * N
    w.sort(reverse=True)
    t.sort(reverse=True)

    result = 0
    for i in range(M):
        for j in range(N):
            if t[i] >= w[j] and not w_on[j]:
                result += w[j]
                w_on[j] = 1
                break

    print(f"#{tc} {result}")
