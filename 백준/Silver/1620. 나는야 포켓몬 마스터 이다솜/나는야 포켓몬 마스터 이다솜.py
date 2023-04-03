import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = {}
num = {}
for i in range(N):
    # 포켓몬 이름
    p = input().rstrip()
    name[p] = i+1
    num[i+1] = p

for _ in range(M):
    ques = input().rstrip()
    if ques.isnumeric():
        print(num[int(ques)])
    else:
        print(name[ques])