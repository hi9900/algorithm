import sys
input = sys.stdin.readline

# 중앙값: 크기 순으로 놓았을 때, 가장 중앙에 놓인 값
lst = [0] * 5
for i in range(5):
    lst[i] = int(input())

lst.sort()

print(sum(lst) // 5)
print(lst[2])
