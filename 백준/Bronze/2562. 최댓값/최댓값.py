max_N = 0
max_i = 0

for i in range(1, 10):
    N = int(input())
    if max_N < N:
        max_N = N
        max_i = i

print(max_N)
print(max_i)