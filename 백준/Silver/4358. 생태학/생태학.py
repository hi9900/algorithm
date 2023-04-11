import sys
from collections import defaultdict
input = sys.stdin.readline

tree_dict = defaultdict(int)
cnt = 0
while 1:
    data = input().rstrip()
    if not data:
        break
    tree_dict[data] += 1
    cnt += 1

data = list(zip(tree_dict.keys(), tree_dict.values()))
data.sort()
# print(data)
for k, v in data:
    print(f"{k} {100 * v / cnt:0.4f}")