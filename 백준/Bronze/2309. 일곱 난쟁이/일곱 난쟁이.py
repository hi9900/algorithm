import sys
input = sys.stdin.readline

# 7난쟁이의 키의 합이 100
# 9에서 7개를 고르는 경우 -> 9C7 = 9C2 = 9*8/2 = 36 완탐ㄱㄱ
lst = []
for _ in range(9):
    lst.append(int(input()))

# 9난쟁이의 합 - 100 만큼 2개가 빠져야 함
cha = sum(lst) - 100

for i in range(9):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == cha:
            # 뒤에꺼 먼저 제거
            lst.remove(lst[j])
            lst.remove(lst[i])
            break
    if len(lst) == 7:
        break

lst.sort()
print(*lst, sep="\n")