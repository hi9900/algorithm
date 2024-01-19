import sys
input = sys.stdin.readline

N, B = map(int, input().split())
# N = int(result, B)
change = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
          'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z']
result = ''
while 1:
    a, b = divmod(N, B)
    result += change[b]

    if a < B:
        if a == 0:
            break
        result += change[a]
        break

    N = a

print(result[::-1])
