import sys
sys.stdin = open("input.txt")


def solution(m, money):
    global result

    if result <= money:
        return

    if m > 12:
        result = min(result, money)
        return

    # 1일권
    solution(m+1, money+(cost[0]*month[m-1]))

    # 1달권
    if month[m-1]:
        solution(m+1, money+cost[1])

    # 3달권
    solution(m+3, money+cost[2])

    # 1년권
    solution(m+12, money+cost[3])


T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    month = list(map(int, input().split()))
    result = 10e9
    solution(1, 0)
    print(f"#{tc} {result}")
