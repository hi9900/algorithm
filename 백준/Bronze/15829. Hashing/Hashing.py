import sys
input = sys.stdin.readline

L = int(input())
word = input().rstrip()

r = 31
M = 1234567891

# 영문 소문자 -> 숫자 * r**i -> 합
sum_nums = 0
for i in range(L):
    sum_nums += (ord(word[i]) - 96) * (r ** i)

print(sum_nums % M)
