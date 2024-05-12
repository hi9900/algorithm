S = input()
# 0의 개수 / 1의 개수 -> 절반
# cnt_zero, cnt_one = S.count('0'), S.count('1')
cnt_zero, cnt_one = S.count('0') // 2, S.count('1') // 2

# 사전순 -> 0 -> 1
print('0' * cnt_zero + '1' * cnt_one)
