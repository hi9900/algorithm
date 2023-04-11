import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())    # 홀수
nums = []
count_dict = defaultdict(int)

for _ in range(N):
    num = int(input())  # 정수
    nums.append(num)
    count_dict[num] += 1
nums.sort()

# 산술평균
avg = sum(nums) / N
print(round(avg))

# 중앙값
mid = N // 2
print(nums[mid])

# 최빈값
count_lst = sorted(list(zip(count_dict.keys(), count_dict.values())), key=lambda x: (-x[1], x[0]))
# print(count_lst)
if len(count_lst) == 1:
    print(count_lst[0][0])
elif count_lst[0][1] == count_lst[1][1]:
    print(count_lst[1][0])
else:
    print(count_lst[0][0])

# 최대최소 차이
print(max(nums)-min(nums))