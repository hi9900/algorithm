import sys
from itertools import permutations
input = sys.stdin.readline

N, M, K = map(int, input().split())
rail = list(map(int, input().split()))


def solve(rail, s, result, answer):
    for i in range(K):
        if result >= answer:
            return answer
        total = 0
        while 1:
            if total + rail[s] > M:
                result += total
                break
            total += rail[s]
            # print(i, s, total)
            s = (s+1) % N

    return min(result, answer)


# 레일 배치 경우의 수
rails = list(permutations(rail, N))
answer = 10e6
for i in rails:
    answer = min(answer, solve(i, 0, 0, answer))

print(answer)