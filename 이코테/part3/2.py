S = input()

result = int(S[0])
for i in S[1:]:
    i = int(i)
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
