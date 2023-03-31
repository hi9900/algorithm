import sys
sys.stdin = open("input.txt")


def sol(arr, N):
    global cnt
    for i in range(1, 1 << N):     # 2 ** N
        flag = bin(i)[2:].zfill(N)  # str
        # subset=[]
        ans = 0
        for j in range(N):
            if flag[j] == "1":
                # subset.append(arr[j])
                ans += int(arr[j])

            if ans > K:
                break

        if ans == K:
            cnt += 1
        # result.append(subset)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    cnt = 0
    sol(A, N)
    print(f"#{tc} {cnt}")
