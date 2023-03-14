import sys
input = sys.stdin.readline


def numnum(N2):
    cnt = 2
    nums = [N, N2]

    while 1:
        N3 = nums[-2] - nums[-1]

        if N3 < 0:
            return cnt, nums
        else:
            cnt += 1
            nums.append(N3)


N = int(input())

mmax = 0
max_lst = []
for N2 in range(1, N+1):
    if numnum(N2)[0] > mmax:
        mmax = numnum(N2)[0]
        max_lst = numnum(N2)[1]

print(mmax)
print(*max_lst)