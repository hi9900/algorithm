S = input()

result = 1
for i in S:
    i = int(i)
    if i == 0:
        continue

    result *= i

print(result)
