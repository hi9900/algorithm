import sys
sys.stdin = open("input.txt")


def b_search(lst, target):
    l = 0
    r = len(lst)-1
    m = (l+r) // 2

    if l > r:
        return 0

    else:
        if target == lst[m]:
            x.append("m")
            return 1

        elif target < lst[m]:
            if x and x[-1] == "L":
                return 0
            x.append("L")
            return b_search(lst[l:m], target)

        elif target > lst[m]:
            if x and x[-1] == "R":
                return 0
            x.append("R")
            return b_search(lst[m+1:r+1], target)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0

    for i in range(M):
        x = []

        if b_search(A, B[i]):
            cnt += 1
        #     print(tc, i, x)
        # else:
        #     print(tc, i, x)
    print(f"#{tc} {cnt}")
