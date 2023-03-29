import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * N
    for _ in range(N):
        s, e = map(int, input().split())
        lst[_] = (e, s)
    lst.sort()

    select = [lst[0]]
    cnt = 1
    for i in range(1, N):
        # 종료시각과 시작시각이 앞의 종료시간보다 같거나 긺
        if lst[i][0] >= select[-1][0] and lst[i][1] >= select[-1][0]:
            cnt += 1
            select.append(lst[i])

    print(f"#{tc} {cnt}")
