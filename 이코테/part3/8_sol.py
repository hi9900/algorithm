S = input()
n = 0
result = []

for c in S:
    if c.isnumeric():
        n += int(c)
    else:
        result.append(c)

result.sort()

if len(result) != len(S):
    result.append(str(n))

print("".join(result))
