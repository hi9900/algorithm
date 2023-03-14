import sys
input = sys.stdin.readline

N = int(input())
card = tuple(map(int, input().split()))
M = int(input())
num = tuple(map(int, input().split()))

result = {}
for i in card:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

# ans = [0] * M
# for i in range(M):
#     if num[i] in result:
#         ans[i] += result[num[i]]

# print(*ans)
print(' '.join(str(result[key])
      if key in result else '0' for key in num))