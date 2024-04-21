N = input()

"""
2진수 N -> 8진수
1. 2진수 N -> 10진수
2. 10진수 -> 8진수
"""
# 1
number = int('0b'+N, 2)
# 2
print(oct(number)[2:])