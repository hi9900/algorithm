import sys
sys.stdin = open("input.txt")


def m_sort(s, e):
    global cnt
    m = (s+e+1)//2

    if s == e:
        return

    m_sort(s, m-1)
    m_sort(m, e)

    ## merge()
    k = 0
    # 왼쪽과 오른쪽에서 가장 작은 숫자(앞)의 위치
    l, r = s, m
    if data[r-1] > data[e]:
        cnt += 1

    while l <= m-1 or r <= e:
        if l <= m-1 and r <= e:
            if data[l] <= data[r]:
                tmp[k] = data[l]
                l += 1
            else:
                tmp[k] = data[r]
                r += 1
            k += 1
        elif l <= m-1:
            while l <= m-1:
                tmp[k] = data[l]
                l += 1
                k += 1
        elif r <= e:
            while r <= e:
                tmp[k] = data[r]
                r += 1
                k += 1
    i = 0
    while i < k:
        data[s+i] = tmp[i]
        i += 1

    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    tmp = [0] * N

    cnt = 0
    # ans = merge_sort(data, N)
    m_sort(0, N-1)
    print(f"#{tc}", data[N//2], cnt)
    # print(f"#{tc} {ans[N//2]} {cnt}")
