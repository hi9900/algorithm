import sys
input = sys.stdin.readline

total = 0
for i in range(5):
    start, end = map(str, input().split())

    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))

    time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
    total += time

print(total)
    