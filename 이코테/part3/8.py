S = input()
word = []
result = 0
for i in S:
    if i.isnumeric():
        result += int(i)
    else:
        word.append(i)

word.sort()
print(*word, result, sep="")
