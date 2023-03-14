N = int(input())

result = dict()
for i in range(N):
    k, v = input().split()
    result[int(k)] = result.get(int(k), []) + [v]

age_sort = sorted(result.items())

for i in age_sort:
    for j in i[1]:
        print(int(i[0]), j)