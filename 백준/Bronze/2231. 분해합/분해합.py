import sys
input = sys.stdin.readline

N = int(input())

# 생성자 + 각 자리수의 합 = 분해합 N
for i in range(1, N+1):

    # i 와 i의 각 자리수의 합 == N
    num = [int(j) for j in str(i)]
    if i + sum(num) == N:
        print(i)
        break
else:
    print(0)
    