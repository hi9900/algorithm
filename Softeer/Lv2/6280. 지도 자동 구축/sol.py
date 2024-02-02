import sys
input = sys.stdin.readline

N = int(input())

# step 0
# 사각형의 수
sqare = 1
# 점의 수
result = 4

for i in range(N):
    result += sqare + (2**(i)+1) * (2 * 2**i)
    sqare *= 4
    
print(result)