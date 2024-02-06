import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 비내림차순; 각각의 원소가 바로 앞에 있는 원소보다 크거나 같은 경우
# A의 원소가 작은 것부터 번호를 매김

# A의 원소 빈도
nums = [0] * 1001
for i in range(N):
    nums[A[i]] += 1

B = [0] * N
for i in range(N):
    B[i] = sum(nums[:A[i]])
    if nums[A[i]] > 1:
        nums[A[i]-1] += 1
        nums[A[i]] -= 1

print(*B)