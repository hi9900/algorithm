import sys
sys.stdin = open("input.txt")

def cross(nums, k, n):
    global result

    if int("".join(nums)) in results[k]:
        return
    else:
        results[k].append(int("".join(nums)))

    if k == n:
        return

    else:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                cross(nums, k + 1, n)
                nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T + 1):
    board, N = input().split()
    N = int(N)
    lst = list(board)

    results = [[] for _ in range(N+1)]

    cross(lst, 0, N)
    ans = max(results[-1])
    print(f"#{tc} {ans}")
