"""
# 첫 번째 코드
def solution(food_times, k):
    # k초 전에 다먹음
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    # 완전한 사이클: 다 먹은 음식이 없음
    min_t = min(food_times)
    cycle = k // n + 1
    if min_t >= cycle:
        return k % n + 1

    # 다 먹은 음식이 존재한다면,
    # 일단 무지성
    idx = -1
    # i 초에 먹기 시작하는 음식
    for i in range(k + 1):
        while 1:
            idx += 1
            idx %= n
            # 음식이 있으면 먹방
            if food_times[idx] != 0:
                food_times[idx] -= 1
                break

    return idx + 1

# 채점 결과
# 정확성: 42.9
# 효율성: 7.1
# 합계: 50.0 / 100.0
"""

# 해설 코드
import heapq


def solution(food_times, k):
    # k초 전에 다먹음
    if sum(food_times) <= k:
        return -1

    q = []
    # (음식 시간, 음식 번호)의 형태로 큐에 삽입
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

        # 먹는 데 사용한 시간
    sum_t = 0
    # 직전에 다 먹은 음식 시간
    prev = 0
    # 남은 음식 개수
    n = len(food_times)

    # 먹은 시간 + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수
    while sum_t + (q[0][0] - prev) * n <= k:
        # 현재 음식 시간
        now = heapq.heappop(q)[0]

        # 현재 음식을 먹는 데 걸리는 시간 = (현재 시간 - 이전 시간) * 현재 음식 개수
        sum_t += (now - prev) * n
        n -= 1

        prev = now

    # 남은 음식을 번호 순으로 확인
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_t) % n][1]
