import sys
sys.stdin = open("input.txt")


# 3진수 만들기
def triplet(n, result):
    if n == 0:
        return result

    n, save = divmod(n, 3)
    result += str(save)
    return triplet(n, result)


T = int(input())
for tc in range(1, T+1):
    b_num = (input())     # 2
    t_num = input()     # 3
    max_t = int("2"*len(t_num), 3)
    N = len(b_num)
    btn = int(b_num, 2)

    for i in range(N-1, -1, -1):
        if b_num[i] == "1":
            check = btn-(2**(N-i-1))

        elif b_num[i] == "0":
            check = btn+(2**(N-i-1))

        if max_t < check:
            continue

        b_tri = triplet(check, "")
        b_tri = b_tri[::-1].zfill(len(t_num))

        cnt = 0
        for j in range(len(t_num)):
            if cnt > 1:
                break
            if b_tri[j] != t_num[j]:
                cnt += 1

        else:
            if cnt == 1:
                ans = check
                break

    print(f"#{tc} {ans}")
