import sys
input = sys.stdin.readline
color = []
num = []
num_cnt = [0] * 10
for _ in range(5):
    c, n = input().split()
    color.append(c)
    num.append(int(n))
    num_cnt[int(n)] += 1
col_set = set(color)
num_set = set(num)

check = sorted(num)
result = 100 + check[-1]

if len(col_set) == 1 and check[4] - check[0] == 4:
    result = 900 + check[4]

elif max(num_cnt) == 4:
    result = 800 + num_cnt.index(4)

elif max(num_cnt) == 3 and len(num_set) == 2:
    result = 700 + 10 * num_cnt.index(3) + num_cnt.index(2)

elif len(col_set) == 1:
    result = 600 + check[4]

elif check[4] - check[0] == 4:
    result = 500 + check[4]
elif max(num_cnt) == 3:
    result = 400 + num_cnt.index(3)
elif max(num_cnt) == 2 and len(num_set) == 3:
    result = 300 + check[3] * 10 + check[1]
elif max(num_cnt) == 2:
    result = 200 + num_cnt.index(2)
else:
    result = 100 + check[-1]

print(result)