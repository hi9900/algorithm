import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 제한 구간 및 속도
data = deque()

for _ in range(N):
    L, limit = map(int, input().split())
    data.append((L, limit))

result = 0
# 테스트 구간 및 속도
test = deque()
for _ in range(M):
    L, V = map(int, input().split())
    test.append((L, V))

re = 0

check_L, check_V = data.popleft()
test_L, test_V = test.popleft()

while 1:
    result = max(result, test_V - check_V)
    re = check_L - test_L


    # 검사 끝이면 종료
    if len(data) == 0 and len(test) == 0:
        # print(re)
        break

    # 0보다 크면, 그 구간에서 다음 테스트 검사
    if re > 0:
        test_L, test_V = test.popleft()
        check_L = re
    # 0이면 다음 구간에서 다음 테스트 검사
    elif re == 0:
        test_L, test_V = test.popleft()
        check_L, check_V = data.popleft()
    # 0보다 작으면, 다음 구간에서 그 테스트 검사
    else:
        check_L, check_V = data.popleft()
        test_L = -re

print(result)