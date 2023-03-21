import sys
input = sys.stdin.readline

while 1:
    N = int(input())
    if N == -1:
        break
    data = []
    for i in range(1, N):
        if N % i == 0:
            data.append(i)

    if sum(data) == N:
        print(f"{N} = ", end="")
        print(*data, sep=" + ")

    else:
        print(f"{N} is NOT perfect.")