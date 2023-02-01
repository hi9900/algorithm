import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):
    # 건물의 개수
    N = int(input())
    # N개 건물의 높이 [0,0, ..., 0,0]
    h = list(map(int, input().split()))

    # 초기값 설정
    count = 0
    # 인덱스 값 2 -> N-3 (양 끝의 00 제외)
    for i in range(2, N-2):     # 2 -> N-3
        # 양쪽 2개 중 최댓값 찾기 (h[i]는 제외)
        # 초기값 = 0: 항상 양수
        i_max = 0
        for j in range(i-2, i+3):  # i-2, i-1, (i), i+1, i+2
            if j == i:
                pass
            elif h[j] > i_max:
                i_max = h[j]
        # h[i] - 최댓값 이 양수인 값만 카운트업
        if (h[i] - i_max) > 0:
            count += (h[i] - i_max)
    print(f'#{test_case} {count}')
