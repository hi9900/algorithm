import sys
input = sys.stdin.readline

# 2007년 1월 1일 월요일
# 월 화 수 목 금 토 일
# 1 2 3 4 5 6 7(0) -> 7로 나눈 나머지

# 월 별 마지막 날짜 31 28 31 30 31 30 31 31 30 31 30 31
endDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# ex) 3월 14일 -> (31+28) + 14 = 73 -> 73 % 7 = 3 -> 수요일

x, y = map(int, input().split())
d = y
for i in range(x):
    d += endDay[i]

d %= 7
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day[d])
