import sys
from collections import deque
input = sys.stdin.readline


def func(x):
    global n, R
    if x == "R":
        R += 1

    elif x == "D":
        n -= 1
        if R % 2:
            arr.pop()
        else:
            arr.popleft()


T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    # arr 받기
    arr = input().rstrip()[1:-1].split(",")
    arr = deque(arr)
    if n == 0:
        arr = []
    arrow = "left"
    R = 0
    for i in p:
        if i == "D" and n == 0:
            print("error")
            break
        func(i)

    else:
        if R % 2:
            arr.reverse()
        print(f"[{','.join(arr)}]")
