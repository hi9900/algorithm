import sys
input = sys.stdin.readline


def round(n):
    if n - int(n) >= 0.5:
        return int(n//1) + 1
    else:
        return int(n)


N = int(input())

# 모든 사람의 난이도 의견의 30% 절사평균
# 가장 큰 값과 가장 작은 값을 제외한 평균 -> 위에서 15%, 아래에서 15%를 제외한 평균(소수점반올림)
a = [0] * N
for _ in range(N):
    a[_] = int(input())

if len(a) == 0:
    print(0)
else:
    a.sort()
    # 제외
    no = round(N * 0.15)
    # 계산된 평균도 반올림
    avg_a = round(sum(a[no:N-no]) / (N - no * 2))
    print(avg_a)
