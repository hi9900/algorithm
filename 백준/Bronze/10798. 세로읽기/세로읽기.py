data = [list(input()) for _ in range(5)]
result = [[] for _ in range(15)]

for i in range(5):
    for j in range(len(data[i])):
        result[j].append(data[i][j])

for i in result:
    if i == []:
        break
    print(*i, sep="", end="")
   