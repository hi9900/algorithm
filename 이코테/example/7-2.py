N = int(input())
data = [0] + list(map(int, input().split()))
d = [0] * 101

d[1] = data[1]
for i in range(2, N+1):
    d[i] = max(d[i-1], d[i-2]+data[i])

print(d[N])
