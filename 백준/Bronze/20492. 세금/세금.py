import sys
input = sys.stdin.readline

N = int(input())
# 전체 상금의 22%를 제세공과금으로 납부
print(f'{N - N * 0.22:.0f}', end=" ")

# 상금의 80%를 제외한 22%를 제세공과금으로 납부
print(f'{N - N * 0.2 * 0.22:.0f}')
