import sys
input = sys.stdin.readline

d = int(input())
cars = list(map(int, input().split()))

print(cars.count(d))
