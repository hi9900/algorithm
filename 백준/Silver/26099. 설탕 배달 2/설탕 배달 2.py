import sys
input = sys.stdin.readline

N = int(input())
result = -1
five_max, three = divmod(N, 5)

for i in range(five_max, -1, -1):
    if divmod(N-5*i, 3)[1] == 0:
        three_n = divmod(N-5*i, 3)[0]
        result = i + three_n
        break

print(result)