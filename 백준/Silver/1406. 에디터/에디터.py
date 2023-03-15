import sys
input = sys.stdin.readline

# 커서 앞 데이터
data_f = list(input().rstrip())
# 커서 뒤 데이터, 역순
data_b = []
M = int(input())

for _ in range(M):
    do = input().split()
    if "L" in do:
        if data_f:
            data_b.append(data_f.pop())
    elif "D" in do:
        if data_b:
            data_f.append(data_b.pop())
    elif "B" in do:
        if data_f:
            data_f.pop()
    elif "P" in do:
        data_f.append(do[-1])

print(*data_f, *data_b[::-1], sep="")