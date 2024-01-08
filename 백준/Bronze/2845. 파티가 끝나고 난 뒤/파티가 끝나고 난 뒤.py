import sys
input = sys.stdin.readline

L, P = map(int, input().split())
data = list(map(int, input().split()))

# L * P = 전체 사람 수
know = L * P
for i in data:
    print(i - know, end=" ")
    