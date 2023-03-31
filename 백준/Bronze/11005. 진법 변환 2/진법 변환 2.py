import sys
input = sys.stdin.readline

N, B = map(int, input().split())

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
       "A", "B", "C", "D", "E", "F",
       "G", "H", "I", "J", "K", "L",
       "M", "N", "O", "P", "Q", "R",
       "S", "T", "U", "V", "W", "X", "Y", "Z"]

result = []
while 1:
    if N < B:
        result.append(num[N])
        break

    N, plus = divmod(N, B)

    result.append(num[plus])
print(*result[::-1], sep="")