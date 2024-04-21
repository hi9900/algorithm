N = input()

"""
8진수 N -> 2진수
1. 8진수 N -> 10진수
2. 10진수 -> 2진수
"""
# 1
# 8진수는 '0o'가 붙음: oct
number = int('0o'+N, 8)
# 2
# 2진수는 '0b'가 붙음: bin
print(bin(number)[2:])