import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))
for _ in range(K):
    A, B = map(int, input().split())

    avg = sum(scores[A-1:B]) / (B-A+1)
    print(f'{avg:.2f}')