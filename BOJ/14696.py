# https://www.acmicpc.net/problem/14696
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, *data_a = map(int, input().split())
    b, *data_b = map(int, input().split())

    # 별 4
    # 동그라미 3
    # 네모 2
    # 세모 1
    # 무승부
    if data_a.count(4) > data_b.count(4):
        win = "A"
    elif data_a.count(4) < data_b.count(4):
        win = "B"
    elif data_a.count(3) > data_b.count(3):
        win = "A"
    elif data_a.count(3) < data_b.count(3):
        win = "B"
    elif data_a.count(2) > data_b.count(2):
        win = "A"
    elif data_a.count(2) < data_b.count(2):
        win = "B"
    elif data_a.count(1) > data_b.count(1):
        win = "A"
    elif data_a.count(1) < data_b.count(1):
        win = "B"
    else:
        win = "D"

    print(win)