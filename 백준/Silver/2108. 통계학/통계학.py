import math
import sys
input = sys.stdin.readline

N = int(input())
nums = []
dict_nums = dict()
for _ in range(N):
    num = int(input())

    nums.append(num)

    if num in dict_nums:
        dict_nums[num] += 1
    else:
        dict_nums[num] = 1

# 1. 산술평균
print(math.floor(sum(nums) / N + 0.5))

# 2. 중앙값
sort_nums = sorted(nums)
print(sort_nums[N // 2])

# 3. 최빈값
dict_nums_list = sorted(list(zip(dict_nums.keys(), dict_nums.values())), key=lambda x: (-x[1], x[0]))
if len(dict_nums_list) >= 2 and dict_nums_list[0][1] == dict_nums_list[1][1]:
    print(dict_nums_list[1][0])
else:
    print(dict_nums_list[0][0])

# 4. 범위
print(max(nums) - min(nums))
