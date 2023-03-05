# https://www.acmicpc.net/problem/1244
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    s, i = map(int, input().split())
    # s == 1; 남
    if s == 1:
        for num in range(N):
            if (num+1) % i == 0 and data[num] == 0:
                data[num] = 1
            elif (num+1) % i == 0 and data[num] == 1:
                data[num] = 0
    elif s == 2:
        i -= 1
        if data[i] == 1:   data[i] = 0
        elif data[i] == 0:  data[i] = 1

        for num in range(1, N+1):
            if i+num >= N or i-num < 0:
                break
            elif data[i+num] == data[i-num]:
                if data[i + num] == 0:  data[i+num], data[i - num] = 1, 1
                elif data[i + num] == 1:  data[i+num], data[i - num] = 0, 0
            elif data[i + num] != data[i - num]:
                break

# print(data)
for idx in range(0, N+1, 20):
    print(*data[idx:idx+20])
