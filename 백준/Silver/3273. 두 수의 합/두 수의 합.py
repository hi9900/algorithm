import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
x = int(input())

check = [0] * 2000001
cnt = 0
for i in range(N):
    if check[x-data[i]] == 1:
        cnt += 1
    
    check[data[i]] += 1

print(cnt)    
