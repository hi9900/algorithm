import sys
input = sys.stdin.readline

# 각 자리가 등차 수열을 이루는 수 : 한수
N = int(input())
cnt = 0
for i in range(1, N+1):
    i = str(i)
    # i가 2자리 수보다 작으면, 한수
    if len(i) <= 2:
        cnt += 1
        continue

    # 3자리수 이상이라면, 첫 두자리수의 차이만큼 일정하면, 한수
    check = int(i[1]) - int(i[0])
    for j in range(1, len(i)-1):
        if int(i[j+1]) - int(i[j]) != check:
            break
    else:
        cnt += 1

print(cnt)
