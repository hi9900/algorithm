import sys
input = sys.stdin.readline

# n + n의 각 자리수 = d(n)
# n: 생성자
nums = [0] * 10001

# 생성자가 없는 숫자 = 셀프넘버
for i in range(1, 10001):
    # i + i의 각 자릿수의 합
    sum_i = i
    for j in str(i):
        sum_i += int(j)
        if sum_i > 10000:
            break
    else:
        nums[sum_i] += 1

for i in range(1,10001):
    if nums[i] == 0:
        print(i)
        