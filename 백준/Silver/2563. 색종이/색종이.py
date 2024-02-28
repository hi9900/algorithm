N = int(input())

data = [[0] * 101 for _ in range(101)]
result = 0
for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            if data[i][j] == 0:
                data[i][j] += 1
                result += 1
print(result)