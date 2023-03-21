import sys
input = sys.stdin.readline

def baek(N):
    if N == 1:
        return
    for i in insu:
        if N % i == 0:
            print(i)
            return baek(N//i)

N = int(input())

insu = []

for i in range(2, N+1):
    if N % i == 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            insu.append(i)
insu.append(N)

baek(N)

