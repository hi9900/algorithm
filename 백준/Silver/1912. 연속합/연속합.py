n = int(input())
arr = list(map(int, input().split()))

max_result = arr[0]
cur_result = arr[0]

for a in arr[1:]:
    cur_result = max(cur_result + a, a)
    max_result = max(max_result, cur_result)

print(max_result)
