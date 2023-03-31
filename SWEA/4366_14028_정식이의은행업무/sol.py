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
    b_num = list(input())     # 2
    t_num = input()     # 3
    max_t = int("2"*len(t_num), 3)
    hoxy = []

    for i in range(len(b_num)):
        # 2진수를 한자리씩 바꿔서 저장하기 -> 2진수값의 길이만큼(<40)
        if b_num[i] == "1":
            b_num[i] = "0"
            hoxy.append("".join(b_num))
            b_num[i] = "1"
        elif b_num[i] == "0":
            b_num[i] = "1"
            hoxy.append("".join(b_num))
            b_num[i] = "0"
    # print(hoxy)

    for b in hoxy:
        b = int(b, 2)   # 2 -> 10진수
        if max_t < b:
            continue

        b_tri = triplet(b, "")
        b_tri = (b_tri[::-1])   # 3진수
        b_tri = b_tri.zfill(len(t_num))

        # print(b_tri, t_num)
        # 저장된 2진수를 3진수로 바꿨을 때, 한자리만 다르면 그거임
        cnt = 0
        for i in range(len(t_num)):
            if cnt > 1:
                break
            if b_tri[i] != t_num[i]:
                cnt += 1
                idx = i

        if cnt == 1:
            ans = b
            break

    print(f"#{tc} {ans}")
