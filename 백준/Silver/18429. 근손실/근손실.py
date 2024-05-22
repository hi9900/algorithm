from itertools import permutations

N, K = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for permutate in permutations(lst):
    kg = 0

    for i in permutate:
        kg = kg - K + i
        if kg < 0:
            break
    else:
        result += 1

print(result)
