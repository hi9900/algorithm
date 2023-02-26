import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A

    # 길이 짧은게 N, A

    mul = [0] * M

    ans = 0
    # A: 0 -> M-N+1;
    for i in range(N):
        for j in range(i, i+(M-N+1)):
            mul[j-i] += A[i] * B[j]
            # print(i, j)
    # print(mul)
    print(f"#{tc} {max(mul)}")

