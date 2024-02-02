import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    S, T = input().split()

    # 모두 대문자로 변환
    S = S.upper()
    T = T.upper()

    # S에서 X가 등장하는 위치
    idx = S.index('X')

    # T에서 해당 인덱스 문자
    print(T[idx], end="")