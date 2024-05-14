import sys
input = sys.stdin.readline

N, M = map(int, input().split())

all_name1 = dict()
all_name2 = dict()

for _ in range(N):
    name = input().rstrip()
    all_name1[_+1] = name
    all_name2[name] = _+1

for _ in range(M):
    question = input().rstrip()
    
    # 숫자면, 해당 번호의 포켓몬 출력
    if question.isnumeric():
        print(all_name1[int(question)])
    # 알파벳이면, 포켓몬 번호 출력
    else:
        print(all_name2[question])
