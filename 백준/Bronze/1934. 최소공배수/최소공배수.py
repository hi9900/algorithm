import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    # A와 B의 최대 공약수 구하기
    for i in range(min(A, B), 1, -1):
        if A % i == 0 and B % i == 0:
            print(i * (A//i) * (B//i))
            break

    else:
        print(A * B)
