import sys
input = sys.stdin.readline

# 대문자 단어
word = input()

time = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}

result = 0
for i in word:
    for j in time:
        if i in j:
            result += time[j]

print(result)