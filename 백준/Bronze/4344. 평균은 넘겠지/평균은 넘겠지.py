import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N, *arr = map(int, input().split())

    # 평균 구하기
    avg = sum(arr) / N

    # 평균을 넘는 학생 수
    cnt = 0
    for i in range(N):
        if arr[i] > avg:
            cnt += 1

    # 비율
    print(f'{cnt/N*100:.3f}%')