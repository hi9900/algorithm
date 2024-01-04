N = int(input())

info = []

for _ in range(N):
    name, score = input().split()
    info.append((name, int(score)))


# def sorting(data):
#     return data[1]
#
#
# info.sort(key=sorting)

# 람다 함수 사용
info.sort(key=lambda x: x[1])

for i in range(N):
    print(info[i][0], end=" ")
